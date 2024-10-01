

import win32clipboard
from markdownify import markdownify
import win32
import unicodedata
import re, sys
from copy import copy
from dataclasses import dataclass


def main():
	text = get_text_from_clipboard()
	text = remove_blank_lines(text)
	text = remove_new_lines_from_multiline_math_formulas(text)
	text = aggregate_multiline_math_formulas(text)
	# print(text); return #TO BE USED FOR DEBUGGING
	text = handle_titles(text)
	text = format_inline_math_formulas(text)
	text = modify_tabs_into_stair_format(text) 
	text = add_brake_lines_after_inline_points(text) 
	text = trasform_text_into_a_bullet_list(text) 
	text = add_one_indentation_to_each_line(text)
	text = add_line_separator(text)
	special_print(text)
	return



DEBUG = True # Remeber to set it to False

def Test(): 
	tests = [None, Test_1, Test_2, Test_3, Test_4]
	tests[4]()





# FORMAT = 1
# FORMAT = 7
# FORMAT = 13 # Simple markdown
# FORMAT = 16
# FORMAT = 49780
# FORMAT = 49265 # WOWDirChange
# FORMAT = 49285 # HTML Format
	
POSSIBLE_CHATGPT_TEXT_FORMATS = [
	49265,
	49285,
	49290,
]
OBSIDIAN_TEXT_FORMAT = 13

""" 
#TODO (or not)
format_equation_rules = [
	# An "equation" is a substring that:
	# 	starts with "$" and end with "$" (inline equation)
	# 	or starts with "$$" and end with "$$" (equation)

	# Numbers are always considerated as an equation or parts of one,
	# but they do not begin with "$", same with signs : 
	# "-", "+", "*", "^", ecc.

	# If two distinct INLINE equations are concatenated, join them
	#	~Ex.: $\alpha$$\beta$ must become $\alpha\beta$
	#	~Ex.: $\alpha$ $\beta$ must become $\alpha \beta$

	# Titles: '# Aaaa', '## Aaaa', ... '####### Aaaa', needs to be 
	# transformed into italic-bold ***Aaaa***, and add one indentation 
	# level under them

	# Numeric Lists: '1.', '2.', ..., need to be created with 2 spaces
	# before the number, and not a whole indentation level

]
"""



def divide_text_into_matches_and_inbetweens(text, matches):
	k = 0
	end = 0
	splitted_text = list()
	for match in matches:
		start, end = match.span()
		if start == 0: splitted_text.append('')
		else: splitted_text.append(text[k:start])
		k = end
	if end != len(text): splitted_text.append(text[end:])
	else: splitted_text.append('')
	assert len(splitted_text) == len(matches) + 1
	return splitted_text, matches



def is_title(line):
	pattern = r'^(#{1,6})\s+(.*?)$'
	matches = list(re.finditer(pattern, line.lstrip()))
	if not matches: return False
	else: return True


def is_bullet_list(line):
	pattern = r'^[\*\-\+]\s+(.+)$'
	matches = list(re.finditer(pattern, line.lstrip()))
	if not matches: return False
	else: return True


def is_inline_math_formula(line):
	pattern1 = r'\\\((.*?)\\\)'
	pattern2 = r'\$(.*?)\$'
	matches1 = list(re.finditer(pattern1, line.lstrip()))
	matches2 = list(re.finditer(pattern2, line.lstrip()))
	if not matches1 and not matches2: return False
	else: return True


def is_multiline_math_formula(line):
	pattern1 = r'\\\[(.*?)\\\]'
	pattern2 = r'\$\$(.*?)\$\$'
	matches1 = list(re.finditer(pattern1, line.lstrip()))
	matches2 = list(re.finditer(pattern2, line.lstrip()))
	if not matches1 and not matches2: return False
	else: return True


# is_numeric_list is already declerad!!!



def remove_blank_lines(text):
	lines = text.split('\n')
	text = ''
	strip = lambda split: split.lstrip().rstrip()
	for line in lines:
		if strip(line) != '': text += line + '\n'
	if text[-1] == '\n': text = text[:-1]
	return text



def remove_new_lines_from_multiline_math_formulas(text):
	pattern = r'\\\[(.*?)\\\]'
	matches = list(re.finditer(pattern, text, re.DOTALL))
	if not matches: return text
	splitted_text, matches = divide_text_into_matches_and_inbetweens(text, matches)
	splitted_text += ('',)

	strip = lambda split: split.lstrip().rstrip()
	get_last_line = lambda split_text_i: strip(split_text_i).split('\n')[-1]
	get_first_line = lambda split_text_i: strip(split_text_i).split('\n')[0]

	text = ''
	for i in range(len(splitted_text)-1):
		if i == 0: 
			text += strip(splitted_text[i])
			# print(f">>> stripped_text[{i}]:\n{strip(splitted_text[i])}")
			continue

		line_before_formula = get_last_line(splitted_text[i-1])
		prev_formula = '$$'+matches[i-1].group(1).lstrip().rstrip().replace('\n',' ')+'$$'
		line_after_formula = get_first_line(splitted_text[i])
		# print(f">>> line_before_formula = {line_before_formula}")
		# print(f">>> prev_formula = {prev_formula}")
		# print(f">>> line_after_formula = {line_after_formula}")
		# if is_numeric_list(line_after_formula):	print(f"\t>>> (IS NUMERIC LIST)")
		
		if is_title(line_before_formula):
			text += '\nFormula:'

		if (
			is_title(line_after_formula) or 
			is_bullet_list(line_after_formula) or 
			is_numeric_list(line_after_formula)
		):
			prev_formula += '\n'
		
		text += prev_formula + strip(splitted_text[i])

	return text


def aggregate_multiline_math_formulas(text):
	pattern = r'(\$\$(.*?)\$\$)'
	matches = list(re.finditer(pattern, text, re.DOTALL))
	if not matches: return text
	splitted_text, matches = divide_text_into_matches_and_inbetweens(text, matches)
	# print(splitted_text)

	text = ''
	combined_formula = ''
	indices_to_combine = list()
	allowed_chars = [' ', '\n', '\t', '\r']
	# print(f"len(splitted_text) = {len(splitted_text)}")
	# print(f"len(matches) = {len(matches)}")
	for i in range(len(splitted_text)):
		if i == 0: 
			text += splitted_text[i]
			# print(f">>> splitted_text[{i}]:\n{splitted_text[i]}")
			continue
		# print(f"i = {i}")

		# text_in_between_formulas = splitted_text[i]
		if i < len(matches) and does_str_contains_only_these_chars(
			splitted_text[i], allowed_chars
		):
			# print(">>> INSIDE 'str_contains_only_these_chars'")
			if not combined_formula:
				prev_formula = matches[i-1].group(2).lstrip().rstrip()
				curr_formula = matches[i].group(2).lstrip().rstrip()
				# print(f">>> prev_formula = {prev_formula}")
				# print(f">>> curr_formula = {curr_formula}")
				combined_formula = prev_formula+' \\\\ '+curr_formula
				# print(f">>> combined_formula = {combined_formula}")
			else:
				curr_formula = matches[i].group(2).lstrip().rstrip()
				# print(f">>> curr_formula = {curr_formula}")
				combined_formula += ' \\\\ '+curr_formula
				# print(f">>> combined_formula = {combined_formula}")
			# combined_formula += formula
		elif combined_formula:
			# print(">>> INSIDE 'combined_formula'")
			formula = '$$\\begin{array}{l}'+combined_formula+'\\end{array}$$'
			text += formula + splitted_text[i] 
			# print(f">>> (COMBINED) formula = {formula}")
			# print(f">>> splitted_text[{i}]:\n{splitted_text[i]}")
			combined_formula = ''
		else:
			# print(">>> INSIDE 'else'")
			prev_formula = '$$'+matches[i-1].group(2).lstrip().rstrip()+'$$'
			text += prev_formula + splitted_text[i]
			# print(f">>> (MONO) prev_formula = {prev_formula}\n-----")
			# print(f">>> splitted_text[{i}]:\n{splitted_text[i]}")
	
	# print(text)
	# return
	return text



def does_str_contains_only_these_chars(string, allowed_chars):
    return all(char in allowed_chars for char in string)



def handle_titles(text):
	# 1. Title will be all in the form: ***Title***:
	# 2. After a title, you need to have a brake line '<br>'
	#    And after the brake line, add to it the next line
	pattern = r'^(#{1,6})\s+(.*?)$'
	matches = list(re.finditer(pattern, text, re.MULTILINE))
	if not matches: return text
	# for i, match in enumerate(matches): print(f"match[{i}] = {match}")

	splitted_text, matches = divide_text_into_matches_and_inbetweens(text, matches)
	# for match in matches: print(match)
	# splitted_text += ('',)

	min_headings_lvl = 7
	for match in matches:
		heading = get_heading_from_title_match(match)
		min_headings_lvl = min(min_headings_lvl, len(heading))
	if min_headings_lvl >= 7: return text

	strip = lambda split: split.lstrip().rstrip()
	get_last_line = lambda split_text_i: strip(split_text_i).split('\n')[-1]
	get_first_line = lambda split_text_i: strip(split_text_i).split('\n')[0]
	
	def indent_text(text, indentation_lvl):
		indentation = '\t'*indentation_lvl
		lines = text.split('\n')
		# print(lines)
		# indented_text = f'{indentation}'
		indented_text = f'\n{indentation}'.join(lines)
		# print(indented_text)
		# indented_text = indented_text[:-indentation_lvl]
		return indented_text

	def format_title(title):
		if title[-1] in [',', ';', '.', ':']: title = title[:-1]
		italic_bold_title = '***'+title+'***:'
		return italic_bold_title


	text = ''
	for i in range(len(splitted_text)):
		# print(i, '\n', splitted_text[i].rstrip().lstrip(), '\n')
		if i == 0: 
			text += strip(splitted_text[0])
			if text: text += '\n'
			# print(strip(splitted_text[0]))
			continue

		heading_lvl = len(get_heading_from_title_match(matches[i-1]))
		indentation_lvl = 1 + heading_lvl - min_headings_lvl
		title = strip(matches[i-1].group(2))
		# print(f"title = {title}")
		# print(f"indentation_lvl = {indentation_lvl}")

		if is_numeric_list(title):
			# print(f"N.B.: title '{title}' is NUMERIC LIST")
			start = title.find('. ')+2
			end = len(title)
			title = title[:start] + format_title(title[start:end])
		elif is_bullet_list(title):
			# print(f"N.B.: title '{title}' is NUMERIC LIST")
			pattern = r'^[\*\-\+]\s+(.+)$'
			matches = list(re.finditer(pattern, title))
			title = '- ' + format_title(matches[0].group(1))
		else: 
			title = format_title(title)

		text_after_title = strip(splitted_text[i])
		line_before_title = get_last_line(splitted_text[i-1])
		line_after_title = get_first_line(splitted_text[i])

		if (
			text_after_title.rstrip() == '' or 
			is_numeric_list(line_after_title) or 
			is_bullet_list(line_after_title) or
			is_inline_math_formula(line_after_title) or
			is_multiline_math_formula(line_after_title)
		):
			title += '\n\t'
		else:
			title += '<br>'

		text += '\t'*(indentation_lvl-1) + title

		if text_after_title.rstrip() != '':
			indented_text = indent_text(text_after_title, indentation_lvl)
			# print(indented_text)
			text += indented_text + '\n'


	if text[-1] == '\n': text = text[:-1]
	return text



def get_heading_from_title_match(match):
	heading_and_title = match.group(0)
	title = match.group(2)
	# print(f"headings_and_title = {headings_and_title}")
	# print(f"title = {title}")
	heading = heading_and_title.replace(title, '')[:-1]
	# print(f"headings = {headings}")
	return heading



def format_inline_math_formulas(text):
	pattern = r'\\\((.*?)\\\)'
	matches = list(re.finditer(pattern, text, re.MULTILINE))
	if not matches: return text
	# for i, match in enumerate(matches): print(f"match[{i}] = {match}")
	splitted_text, matches = divide_text_into_matches_and_inbetweens(text, matches)
	text = ''
	for i, match in enumerate(matches):
		formula = '$'+match.group(1).lstrip().rstrip()+'$'
		text += splitted_text[i] + formula
	text += splitted_text[-1]
	return text



def modify_tabs_into_stair_format(text):
	# text = '\t\t\tHello\nHi!\n\tHello' #TO TEST
	# Between two consecutive lines there must be 
	# only a difference of 1 in the number of tabs.
	lines = text.split('\n')
	indentation_lvls = list()
	for line in lines:
		indentation_lvl = len(line) - len(line.lstrip('\t'))
		indentation_lvls.append(indentation_lvl)
		# print(f"Line: '{line.strip()}', Tabs: {num_tabs}")
	# print(indentation_lvls)

	# TESTS (all passed)
	# indentation_lvls, solution = [0, 0, 0, 3, 4], [0, 0, 0, 1, 2]
	# indentation_lvls, solution = [1, 3, 2, 3, 3], [3, 3, 2, 3, 3]
	# indentation_lvls, solution = [1, 1, 3, 1, 1], [1, 1, 2, 1, 1]
	# indentation_lvls, solution = [2, 2, 0, 2, 2], [2, 2, 1, 2, 2]
	# indentation_lvls, solution = [1, 2, 3, 1, 1], [1, 2, 3, 2, 1]
	# indentation_lvls, solution = [3, 3, 3, 1, 1], [3, 3, 3, 2, 1]


	def is_star_vector(indentation_lvls):
		return index_error_for_star_vector(indentation_lvls) == None
	
	def index_error_for_star_vector(indentation_lvls):
		for i in range(1, len(indentation_lvls)):
			if indentation_lvls[i] > indentation_lvls[i-1] + 1: return i
			if indentation_lvls[i] < indentation_lvls[i-1] - 1: return i
		return None

	def add_X_to_index_i(vec, X, i):
		copy_vec = copy(vec)
		copy_vec[i] += X
		return copy_vec

	def brute_force_solution(origina_vec):
		vec = copy(origina_vec)
		for i in range(1, len(vec)):
			if vec[i] > vec[i-1] + 1: vec[i] = vec[i-1] + 1
			if vec[i] < vec[i-1] - 1: vec[i] = vec[i-1] - 1
		return vec

	list_of_possible_solutions = [
		lambda vec, i: add_X_to_index_i(vec, X=vec[i]+1, i=i),
		lambda vec, i: add_X_to_index_i(vec, X=vec[i]-1, i=i),
		lambda vec, i: add_X_to_index_i(vec, X=vec[i-1]+1, i=i),
		lambda vec, i: add_X_to_index_i(vec, X=vec[i-1]-1, i=i),
		lambda vec, i: add_X_to_index_i(vec, X=vec[i]+1, i=i-1),
		lambda vec, i: add_X_to_index_i(vec, X=vec[i]-1, i=i-1),
		lambda vec, i: brute_force_solution(vec)
	]

	# print(f"indentation_lvls = {indentation_lvls}")
	i = index_error_for_star_vector(indentation_lvls)
	# print(f"i = {i}")
	if not i: return text
	for function in list_of_possible_solutions:
		try_vec = function(indentation_lvls, i)
		if is_star_vector(try_vec):
			indentation_lvls = try_vec
			break

	# print(f"(NEW) indentation_lvls = {indentation_lvls}")
	text = ''
	for i, line in enumerate(lines):
		text += '\t'*indentation_lvls[i] + line.lstrip('\t')+'\n'
	text = text[:-1]
	# assert indentation_lvls == solution # Use this to test this function
	return text



def add_brake_lines_after_inline_points(text):
	# text = "1. Error1. Correct_1. Error2.\n2222. Error3. Correct_2. Error4"
	pattern = r"\. "
	matches = list(re.finditer(pattern, text))
	if not matches: return text
	splitted_text, matches = divide_text_into_matches_and_inbetweens(text, matches)

	text = ''
	for i, match in enumerate(matches):
		if is_split_numeric_list(splitted_text[i]): 
			text += splitted_text[i] + match.group(0)
			continue
		else:	
			text += splitted_text[i] + '.<br>'

	text += splitted_text[-1]
	if text[-5:] == '.<br>': text = text[:-4]
	return text



def is_split_numeric_list(split):
	accepted_chars = str(list(range(0, 10)))
	# print(accepted_chars)
	# print(split)
	for char in split[::-1]:
		# print(char)
		if char in accepted_chars: continue
		else: accepted_chars = [' ', '\t', '-', '*', '+']

		if char in accepted_chars: continue
		# elif char == '\n' or char == '<br>': return True
		elif char == '\n': return True
		else: return False
	return True



def is_numeric_list(line):
	pattern = r"\. "
	matches = list(re.finditer(pattern, line))
	if not matches: return False
	start, _ = matches[0].span()
	split = line[0:start]
	return is_split_numeric_list(split)



def trasform_text_into_a_bullet_list(text):
	# Add '- ' at each line after the indentation.
	# If a line alread has '- ', skip it.
	# If a line has '+ ', or '* ', transform it
	# If a line is a numeric line, skip it.
	lines = text.split('\n')
	text = ''
	for line in lines:
		stripped = line.lstrip()
		diff = len(line) - len(stripped)
		chars_to_check = stripped[0:2]
		if chars_to_check == '- ':	text += line
		elif chars_to_check == '* ': text += line[:diff]+'- '+stripped[2:]
		elif chars_to_check == '+ ': text += line[:diff]+'- '+stripped[2:]
		elif is_numeric_list(line):
			if line[diff] not in str([0,1,2,3,4,5,6,7,8,9]):
				text += line[:diff]+'- '+stripped
			else: 
				text += line
		else: text += line[:diff]+'- '+stripped
		text += '\n'
	text = text[:-1]
	return text



def add_one_indentation_to_each_line(text):
	lines = text.split('\n')
	text = ''
	for line in lines:
		text += '\t' + line + '\n'
	# text = text[:-1]
	return text


def add_line_separator(text):
	text += '----\n'
	return text



def special_print(text):
	# This is because the plugin 'shell_command' for
	# Obsidin, has some problems printing with the
	# normal print function, specifically: 'à', 'è', ...
	byte_text = text.encode('utf-8')
	sys.stdout.buffer.write(byte_text)



def send_to_clipboard(clip_type, data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(clip_type, data)
	win32clipboard.CloseClipboard()



def get_text_from_clipboard():
	win32clipboard.OpenClipboard()
	if not is_ClipboradFormat_known(): return

	lines = get_lines_from_clipboard()
	# pretty_print_lines(lines)
	text = '\n'.join(lines)
	return text



def is_ClipboradFormat_known():
	if (
		win32clipboard.EnumClipboardFormats(0) not in POSSIBLE_CHATGPT_TEXT_FORMATS and
		win32clipboard.EnumClipboardFormats(0) != OBSIDIAN_TEXT_FORMAT and
		win32clipboard.CountClipboardFormats() < 10 # text formats are usually 5.
	):
		wrn_msg = f"**WARNING**:"
		wrn_msg += f"\n     ClipboardFormat not found in list of expected one."
		wrn_msg += f"\n     ClipboardFormat is: '{win32clipboard.EnumClipboardFormats(0)}' "
		wrn_msg += f"\n     "
		wrn_msg += f"\n     If the text in the Clipboard is taken from ChatGPT, please add this format "
		wrn_msg += f"\n     in the 'POSSIBLE_CHATGPT_TEXT_FORMATS' list\n"
		print(wrn_msg)
		return False
	return True



def get_lines_from_clipboard():
	markdown_str = ""

	chatgpt_format = POSSIBLE_CHATGPT_TEXT_FORMATS[0]
	for format_code in POSSIBLE_CHATGPT_TEXT_FORMATS:
		if win32clipboard.IsClipboardFormatAvailable(format_code):
			chatgpt_format = format_code
			break

	if win32clipboard.IsClipboardFormatAvailable(chatgpt_format):
		data = win32clipboard.GetClipboardData(chatgpt_format)
		markdown_str = markdownify(data)
		almost_start = markdown_str.find('SourceURL')
		# print(markdown_str)
		start = markdown_str.find("\n", almost_start) + 3
		almost_end = markdown_str.find(chr(0x00))
		end = markdown_str.find(" ", almost_end-5)
		markdown_str = markdown_str[start:end]
		# print(markdown_str)

	elif win32clipboard.IsClipboardFormatAvailable(OBSIDIAN_TEXT_FORMAT):
		markdown_str = win32clipboard.GetClipboardData(OBSIDIAN_TEXT_FORMAT)

	else: print("ERROR: No text found on Clipboard")

	if markdown_str == "": return

	list_of_ignored_first_char = ["", " ", "\n"]

	lines = list()
	for line in markdown_str.split("\n"):
		line = line.replace("\r","")
		if len(line) == 0: continue
		lines.append(line)
	
	return lines


# ------------------------------------------------------------------


def Test_1():
	load_text_1()
	main()
	return True

def Test_2():
	load_text_2()
	main()
	return True

def Test_3():
	load_text_3()
	main()
	return True

def Test_4():
	load_text_4()
	main()
	return True


def Test_formats():
	print(win32clipboard.CountClipboardFormats())
	print(win32clipboard.EnumClipboardFormats(0))
	print(win32clipboard.GetClipboardFormatName(49290))


def load_text(text):
	clip_type = 13
	send_to_clipboard(clip_type, text)

def load_text_1():
	text = """
I **gradi di libertà (DOF, Degrees of Freedom)** si riferiscono al numero di parametri indipendenti che definiscono la configurazione o lo stato di un sistema meccanico. In robotica e biomeccanica, i gradi di libertà descrivono il numero di movimenti indipendenti che un robot o una parte del corpo può compiere nello spazio tridimensionale.

### Definizione Generale

Per un sistema meccanico, ogni **grado di libertà** rappresenta una direzione o un asse lungo il quale il sistema può muoversi o ruotare. Un oggetto libero nello spazio tridimensionale ha 6 gradi di libertà:
- **3 gradi di libertà di traslazione**: Movimento lungo gli assi \\(x\\), \\(y\\), \\(z\\).
- **3 gradi di libertà di rotazione**: Rotazione attorno agli assi \\(x\\), \\(y\\), \\(z\\).

Questi gradi di libertà sono importanti perché determinano la capacità di un sistema di raggiungere una determinata posizione e orientamento nello spazio.

### Tipi di Gradi di Libertà

1. **Gradi di Libertà di Traslazione**:
   - Descrivono lo spostamento lineare di un oggetto lungo gli assi cartesiani \\(x\\), \\(y\\) e \\(z\\).
   - Ogni asse di traslazione aggiunge un grado di libertà.
   
   Un esempio di traslazione lungo un asse è il movimento di un'ascensore, che si sposta verticalmente lungo l'asse \\(z\\).

2. **Gradi di Libertà di Rotazione**:
   - Descrivono la capacità di un oggetto di ruotare attorno agli assi \\(x\\), \\(y\\) e \\(z\\).
   - Ogni asse di rotazione aggiunge un grado di libertà.
   
   Ad esempio, la rotazione della testa attorno al collo rappresenta un grado di libertà di rotazione attorno a un asse verticale.

### Esempio: Movimento in 2D e 3D

- **Punto nel piano 2D**: Un punto su un piano bidimensionale ha **2 gradi di libertà** (può muoversi lungo l'asse \\(x\\) e l'asse \\(y\\)).
  
  Esempio: Una formica che cammina su un foglio di carta può spostarsi lungo due direzioni indipendenti (orizzontale e verticale), quindi ha 2 gradi di libertà.

- **Oggetto nello spazio 3D**: Un oggetto rigido libero nello spazio tridimensionale ha **6 gradi di libertà**: 3 di traslazione (lungo \\(x\\), \\(y\\), \\(z\\)) e 3 di rotazione (attorno a \\(x\\), \\(y\\), \\(z\\)).

  Esempio: Un aereo in volo può muoversi in avanti/indietro (traslazione lungo \\(x\\)), salire/scendere (traslazione lungo \\(z\\)), virare a sinistra/destra (rotazione attorno a \\(z\\), chiamata **yaw**), inclinarsi lateralmente (rotazione attorno a \\(x\\), chiamata **roll**), e inclinarsi verso l'alto o il basso (rotazione attorno a \\(y\\), chiamata **pitch**).

### Esempio di un Braccio Robotico

Un **braccio robotico** è spesso modellato come una **catena cinematica** formata da segmenti rigidi connessi da giunti. Ogni giunto aggiunge gradi di libertà al sistema. In un braccio robotico, i gradi di libertà sono solitamente definiti dai giunti **revoluti** (che permettono la rotazione) o **prismatici** (che permettono la traslazione).

- **Braccio robotico a 6 DOF**: Un braccio robotico con 6 gradi di libertà è uno dei modelli più comuni. I suoi 6 gradi di libertà gli permettono di raggiungere qualsiasi posizione e orientamento nello spazio tridimensionale. Un tipico braccio robotico industriale ha:
  - 3 gradi di libertà per spostare la "mano" (end-effector) in qualsiasi punto dello spazio tridimensionale.
  - 3 gradi di libertà per orientare la mano in qualsiasi direzione.

Ecco come i 6 gradi di libertà potrebbero essere distribuiti in un braccio robotico:
- **3 DOF di rotazione** nei primi giunti, per consentire movimenti del braccio attorno all'origine.
- **3 DOF di rotazione** negli ultimi giunti, per consentire la manipolazione e orientamento dell'end-effector.

### Esempi Pratici

1. **Mano Umana**: 
   - La mano ha molti gradi di libertà. Ad esempio, il polso ha 3 gradi di libertà: flessione/estensione (su/giù), deviazione radiale/ulnare (sinistra/destra), e pronazione/supinazione (rotazione del polso). Ogni dito ha diversi gradi di libertà nei giunti che permettono la flessione e l'estensione delle falangi.

2. **Veicolo**:
   - Un'auto su strada ha **3 gradi di libertà**: traslazione lungo l'asse \\(x\\) (avanti e indietro), traslazione lungo l'asse \\(y\\) (sinistra e destra quando sterza), e rotazione attorno all'asse \\(z\\) (virata in curva, cioè "yaw").

3. **Manipolatore robotico**: 
   - Un manipolatore robotico con **7 gradi di libertà** ha maggiore flessibilità, in quanto può risolvere problemi di cinematica ridondante, cioè può raggiungere la stessa posizione in modi diversi, fornendo maggiore precisione o evitando ostacoli.

### Gradi di Libertà in Sistemi Ridotti

- **Catene cinematiche chiuse**: Se un sistema ha vincoli che limitano i movimenti (come in una catena cinematica chiusa), i gradi di libertà del sistema si riducono. Per esempio, un braccio robotico che opera all'interno di una struttura chiusa potrebbe avere limitazioni di movimento, riducendo il numero di gradi di libertà effettivi.

- **Robot a base mobile**: Se un robot è montato su una base mobile (come un robot su ruote), la base stessa potrebbe avere 2 o 3 gradi di libertà aggiuntivi, aumentando la capacità del sistema di muoversi.

### Sintesi

In sintesi, i **gradi di libertà** descrivono le possibilità di movimento di un sistema meccanico. In robotica, ogni giunto aggiunge un grado di libertà al robot, e la somma totale dei gradi di libertà determina quanto liberamente un robot può muoversi o manipolare oggetti nello spazio.
"""
	load_text(text)
	

def load_text_2():
	text = """
Il **Metodo di Eulero** è un semplice metodo numerico utilizzato per risolvere **equazioni differenziali ordinarie** (ODE). In molte applicazioni, come la robotica e la simulazione fisica, le equazioni differenziali vengono utilizzate per descrivere il movimento e le dinamiche di sistemi complessi. Tuttavia, non sempre esiste una soluzione analitica (esatta) per queste equazioni, quindi si ricorre a metodi numerici come il metodo di Eulero per approssimare la soluzione.

### Concetto del Metodo di Eulero

Il Metodo di Eulero approssima la soluzione di un'equazione differenziale risolvendo iterativamente l'equazione nel tempo. L'idea di base è quella di utilizzare l'informazione sulla **derivata** della funzione in un punto per predire il valore della funzione in un punto successivo.

#### Equazione differenziale di base:

Considera un'equazione differenziale ordinaria di primo ordine:
\\[
\\frac{dy}{dt} = f(t, y)
\\]
Dove:
- \\(y(t)\\) è la funzione incognita che vogliamo approssimare.
- \\(f(t, y)\\) è una funzione nota che descrive il tasso di variazione di \\(y\\) rispetto a \\(t\\).

Il Metodo di Eulero ci permette di stimare i valori di \\(y(t)\\) utilizzando un passo temporale discreto \\(\\Delta t\\).

#### Formula del Metodo di Eulero:

Dato un valore iniziale \\(y(t_0)\\) in \\(t_0\\), il metodo di Eulero calcola il valore della funzione nel passo successivo \\(t_1 = t_0 + \\Delta t\\) come:
\\[
y(t_1) = y(t_0) + \\Delta t \\cdot f(t_0, y(t_0))
\\]

Questo processo può essere ripetuto iterativamente per trovare la soluzione approssimata a \\(t_2 = t_1 + \\Delta t\\), \\(t_3 = t_2 + \\Delta t\\), e così via.

### Esempio 1: Crescita della popolazione

Supponiamo di avere un modello molto semplice di crescita della popolazione, dove il tasso di crescita della popolazione è proporzionale alla popolazione stessa. L'equazione differenziale è:
\\[
\\frac{dP}{dt} = r \\cdot P
\\]
Dove \\(P(t)\\) è la popolazione al tempo \\(t\\) e \\(r\\) è la costante di crescita. Supponiamo che inizialmente, \\(P(0) = 100\\) e che \\(r = 0.1\\).

Applichiamo il Metodo di Eulero con un passo temporale \\(\\Delta t = 1\\):

1. Al tempo \\(t_0 = 0\\), \\(P(0) = 100\\).
   \\[
   P(1) = P(0) + \\Delta t \\cdot r \\cdot P(0) = 100 + 1 \\cdot 0.1 \\cdot 100 = 110
   \\]
   
2. Al tempo \\(t_1 = 1\\), \\(P(1) = 110\\).
   \\[
   P(2) = P(1) + \\Delta t \\cdot r \\cdot P(1) = 110 + 1 \\cdot 0.1 \\cdot 110 = 121
   \\]

3. Al tempo \\(t_2 = 2\\), \\(P(2) = 121\\).
   \\[
   P(3) = P(2) + \\Delta t \\cdot r \\cdot P(2) = 121 + 1 \\cdot 0.1 \\cdot 121 = 133.1
   \\]

E così via. Il metodo fornisce un'approssimazione della popolazione nel tempo.

### Esempio 2: Oscillatore armonico semplice

Consideriamo ora un sistema dinamico più complesso, come l'**oscillatore armonico semplice**, che descrive il movimento di una molla o di un pendolo, con l'equazione differenziale:
\\[
\\frac{d^2x}{dt^2} = -\\frac{k}{m}x
\\]
Dove \\(x(t)\\) è la posizione dell'oscillatore, \\(k\\) è la costante elastica della molla, e \\(m\\) è la massa. Questa è un'equazione differenziale del secondo ordine, ma può essere riscritta come un sistema di due equazioni del primo ordine:

1. Definiamo la velocità \\(v(t) = \\frac{dx}{dt}\\), quindi l'equazione diventa:
   \\[
   \\frac{dx}{dt} = v(t)
   \\]
   \\[
   \\frac{dv}{dt} = -\\frac{k}{m}x(t)
   \\]

Applichiamo ora il Metodo di Eulero con passo \\(\\Delta t\\) per calcolare posizione e velocità nel tempo.

Supponiamo che inizialmente la posizione \\(x(0) = 1\\), la velocità \\(v(0) = 0\\), la costante elastica \\(k = 1\\), e la massa \\(m = 1\\).

- Al passo iniziale \\(t_0 = 0\\):
  \\[
  v(1) = v(0) + \\Delta t \\cdot \\left( -\\frac{k}{m}x(0) \\right) = 0 + \\Delta t \\cdot (-1 \\cdot 1) = -\\Delta t
  \\]
  \\[
  x(1) = x(0) + \\Delta t \\cdot v(0) = 1 + \\Delta t \\cdot 0 = 1
  \\]

- Al passo successivo \\(t_1 = t_0 + \\Delta t\\):
  \\[
  v(2) = v(1) + \\Delta t \\cdot \\left( -\\frac{k}{m}x(1) \\right) = -\\Delta t + \\Delta t \\cdot (-1 \\cdot 1) = -2 \\cdot \\Delta t
  \\]
  \\[
  x(2) = x(1) + \\Delta t \\cdot v(1) = 1 + \\Delta t \\cdot (-\\Delta t) = 1 - \\Delta t^2
  \\]
  \\[
  x(3) = \\text{This is only a test}
  \\]

- Test 4
  \\[
  x(4) = \\text{This is only a test (4)}
  \\]

  ### Test 5
  \\[
  x(5) = \\text{This is only a test (5)}
  \\]

Questo processo continua per ogni passo temporale. Il Metodo di Eulero approssima quindi l'andamento dell'oscillatore armonico nel tempo.

### Limiti del Metodo di Eulero

- **Precisione**: Il Metodo di Eulero è relativamente semplice e veloce, ma non è molto preciso, soprattutto se il passo temporale \\(\\Delta t\\) è troppo grande. Errori di approssimazione si accumulano rapidamente.
  
- **Stabilità**: Per alcuni sistemi dinamici, come quelli con oscillazioni rapide (ad esempio l'oscillatore armonico), il metodo può essere instabile se \\(\\Delta t\\) non è abbastanza piccolo.

Per risolvere problemi più complessi con maggiore precisione, si utilizzano metodi numerici più avanzati, come il **Metodo di Eulero Modificato** (o metodo del punto medio) o i metodi **Runge-Kutta**.

Spero che questo chiarisca il concetto di Metodo di Eulero e come viene applicato nella risoluzione numerica di equazioni differenziali!

- #### TEST 6-7
  \\[
  x(6) = \\text{This is only a test (6)}
  \\]
  \\[
  x(7) = \\text{This is only a test (7)}
  \\]
"""
	load_text(text)



def load_text_3():
	text = """
La **regola della mano destra** è una convenzione utilizzata per determinare la direzione del **vettore risultante** di alcuni fenomeni fisici come le rotazioni, i campi magnetici e i momenti torcenti, soprattutto in sistemi tridimensionali. È molto comune in fisica e robotica per descrivere vettori e forze associate a rotazioni e torsioni.

### Applicazioni della Regola della Mano Destra

La regola della mano destra è usata per:
1. **Prodotto vettoriale**: Determinare la direzione del vettore risultante dal prodotto vettoriale di due vettori.
2. **Momento torcente**: Stabilire la direzione del momento torcente (o coppia) generato da una forza applicata a un corpo che può ruotare.
3. **Campi magnetici**: In elettromagnetismo, la regola della mano destra viene usata per determinare la direzione del campo magnetico attorno a un filo percorso da corrente elettrica.

### Come Funziona la Regola della Mano Destra

Per usare la regola della mano destra, segui questi passaggi:

1. **Prodotto vettoriale**:
   Se vuoi determinare la direzione del vettore risultante dal prodotto vettoriale \\(\\mathbf{A} \\times \\mathbf{B}\\):
   - Punta il pollice della mano destra nella direzione del primo vettore \\(\\mathbf{A}\\).
   - Punta l'indice nella direzione del secondo vettore \\(\\mathbf{B}\\).
   - Il medio, perpendicolare al piano formato dai due vettori, indica la direzione del prodotto vettoriale \\(\\mathbf{A} \\times \\mathbf{B}\\).

   Il vettore risultante sarà perpendicolare sia a \\(\\mathbf{A}\\) che a \\(\\mathbf{B}\\) e seguirà la direzione indicata dal medio della mano destra.

   **Esempio**: Se hai due vettori \\(\\mathbf{A}\\) che punta verso destra e \\(\\mathbf{B}\\) che punta verso l'alto, usando la regola della mano destra, il prodotto \\(\\mathbf{A} \\times \\mathbf{B}\\) punta fuori dal piano, verso di te.

2. **Momento torcente**:
   Il **momento torcente** o coppia è il risultato di una forza applicata a una certa distanza da un punto di rotazione. Per determinare la direzione del momento torcente generato da una forza:
   - Punta le dita della mano destra nella direzione della rotazione (cioè nella direzione del movimento circolare).
   - Il pollice, esteso, indicherà la direzione del vettore momento torcente.

   **Esempio**: Se una ruota ruota in senso antiorario, posiziona le dita della mano destra seguendo la rotazione della ruota. Il tuo pollice punterà verso l'alto, indicando che il momento torcente punta verso l'alto lungo l'asse della rotazione.

3. **Campi Magnetici (Legge di Ampère-Maxwell)**:
   Quando una corrente elettrica scorre attraverso un filo, essa genera un **campo magnetico** attorno al filo. La direzione del campo magnetico può essere determinata usando la regola della mano destra:
   - Punta il pollice nella direzione della corrente elettrica.
   - Le dita che si avvolgono attorno al filo indicano la direzione del campo magnetico.

   **Esempio**: Se la corrente scorre verso l'alto attraverso un filo, il campo magnetico si avvolgerà attorno al filo in senso antiorario (guardando dall'alto) seguendo la direzione delle tue dita.

### Esempi di Applicazione

#### 1. Prodotto Vettoriale nella Robotica

Nella robotica, la regola della mano destra viene spesso utilizzata per calcolare la direzione del vettore risultante quando si esegue il **prodotto vettoriale** di due vettori, ad esempio per calcolare la velocità angolare o la forza tangenziale applicata a un braccio robotico.

#### 2. Momento Torcente

In un sistema meccanico, la regola della mano destra viene usata per determinare la direzione del **momento torcente** generato da una forza applicata a un oggetto. Ad esempio, in un'auto, se si gira il volante in senso antiorario, la regola della mano destra indica che il momento torcente agisce verso l'alto.

#### 3. Elettromagnetismo

In elettromagnetismo, la regola della mano destra viene usata per descrivere la relazione tra la corrente elettrica e il campo magnetico. Se si conosce la direzione della corrente in un circuito, la regola della mano destra indica la direzione del campo magnetico indotto.

### Sintesi

La **regola della mano destra** è uno strumento pratico per determinare la direzione di vettori associati a fenomeni rotazionali e campi magnetici, come il prodotto vettoriale, i momenti torcenti e i campi magnetici. È ampiamente utilizzata in fisica, meccanica e robotica per calcolare e visualizzare le direzioni di forze e rotazioni in sistemi tridimensionali.
"""
	load_text(text)



def load_text_4():
	text = """
La **matrice Jacobiana** è uno strumento matematico utilizzato in robotica per descrivere la relazione tra le velocità dei giunti di un robot e la velocità (lineare e angolare) dell'end-effector. La Jacobiana è fondamentale per analizzare e controllare i movimenti dei manipolatori robotici, e permette di calcolare anche le forze e i momenti torcenti sui giunti a partire dalle forze applicate all'end-effector.

### Definizione della Matrice Jacobiana

La **matrice Jacobiana** è una matrice che descrive il tasso di variazione della posizione e dell'orientamento dell'end-effector rispetto ai parametri dei giunti. Essa fornisce una mappatura tra le velocità dei giunti e le velocità dell'end-effector.

In un robot con \\(n\\) gradi di libertà, la matrice Jacobiana \\(J(\\theta)\\) ha dimensioni \\(6 \\times n\\), dove:
- Le prime 3 righe descrivono la **velocità lineare** dell'end-effector rispetto agli assi \\(x\\), \\(y\\) e \\(z\\).
- Le ultime 3 righe descrivono la **velocità angolare** dell'end-effector rispetto agli assi \\(x\\), \\(y\\) e \\(z\\).

In generale, la matrice Jacobiana si ottiene prendendo le derivate parziali della posizione e dell'orientamento dell'end-effector rispetto agli angoli dei giunti.

### Relazione Cinematica

Se consideriamo \\(q = [q_1, q_2, ..., q_n]^T\\) come il vettore degli angoli dei giunti e \\(\\dot{q} = [\\dot{q}_1, \\dot{q}_2, ..., \\dot{q}_n]^T\\) come il vettore delle velocità dei giunti, la **velocità dell'end-effector** \\(v_{eff}\\) è data da:
\\[
v_{eff} = J(q) \\cdot \\dot{q}
\\]

Dove:
- \\(v_{eff}\\) è il vettore di velocità dell'end-effector (che include sia velocità lineare che angolare).
- \\(J(q)\\) è la matrice Jacobiana che dipende dagli angoli dei giunti.
- \\(\\dot{q}\\) è il vettore delle velocità angolari dei giunti.

### Esempio Semplice: Braccio Robotico a 2 Giunti

Consideriamo un **braccio robotico a 2 giunti** revoluti (simile al caso del piano 2D) con lunghezze dei segmenti \\(L_1\\) e \\(L_2\\). Gli angoli dei giunti sono \\(\\theta_1\\) e \\(\\theta_2\\). Vogliamo calcolare la Jacobiana per ottenere la velocità dell'end-effector.

La posizione dell'end-effector \\((x_{\\text{eff}}, y_{\\text{eff}})\\) è data dalle equazioni di cinematica diretta:
\\[
x_{\\text{eff}} = L_1 \\cos(\\theta_1) + L_2 \\cos(\\theta_1 + \\theta_2)
\\]
\\[
y_{\\text{eff}} = L_1 \\sin(\\theta_1) + L_2 \\sin(\\theta_1 + \\theta_2)
\\]

La Jacobiana si ottiene derivando la posizione dell'end-effector rispetto agli angoli \\(\\theta_1\\) e \\(\\theta_2\\):

\\[
J(\\theta) = \\begin{bmatrix}
\\frac{\\partial x_{\\text{eff}}}{\\partial \\theta_1} & \\frac{\\partial x_{\\text{eff}}}{\\partial \\theta_2} \\\\
\\frac{\\partial y_{\\text{eff}}}{\\partial \\theta_1} & \\frac{\\partial y_{\\text{eff}}}{\\partial \\theta_2}
\\end{bmatrix}
= \\begin{bmatrix}
- L_1 \\sin(\\theta_1) - L_2 \\sin(\\theta_1 + \\theta_2) & -L_2 \\sin(\\theta_1 + \\theta_2) \\\\
L_1 \\cos(\\theta_1) + L_2 \\cos(\\theta_1 + \\theta_2) & L_2 \\cos(\\theta_1 + \\theta_2)
\\end{bmatrix}
\\]

Questa è la **matrice Jacobiana** del braccio robotico a 2 giunti. La Jacobiana permette di calcolare la velocità dell'end-effector in termini delle velocità angolari dei giunti \\(\\dot{\\theta_1}\\) e \\(\\dot{\\theta_2}\\):
\\[
\\begin{bmatrix}
\\dot{x}_{\\text{eff}} \\\\
\\dot{y}_{\\text{eff}}
\\end{bmatrix}
= J(\\theta) \\cdot \\begin{bmatrix}
\\dot{\\theta_1} \\\\
\\dot{\\theta_2}
\\end{bmatrix}
\\]
Dove \\(\\dot{x}_{\\text{eff}}\\) e \\(\\dot{y}_{\\text{eff}}\\) rappresentano le componenti della velocità lineare dell'end-effector.

### Forze e Momenti

La Jacobiana non è utile solo per calcolare le velocità, ma anche per analizzare le forze e i momenti nei giunti del robot. Conoscendo la forza applicata all'end-effector, è possibile calcolare i momenti torcenti (\\(\\tau\\)) sui giunti.

Dato un vettore di forze applicate all'end-effector \\(F_{eff}\\), i **momenti torcenti** \\(\\tau\\) sui giunti sono calcolati come:
\\[
\\tau = J^T(q) \\cdot F_{eff}
\\]
Dove \\(J^T(q)\\) è la **trasposta** della Jacobiana.

### Singularità della Matrice Jacobiana

Un concetto importante associato alla Jacobiana è quello delle **singolarità**. Una singolarità si verifica quando la matrice Jacobiana perde rango (il suo determinante diventa zero). In queste condizioni, il robot perde uno o più gradi di libertà nel movimento, e diventa impossibile controllare completamente l'end-effector.

**Esempio di Singolarità**: Nel braccio robotico a 2 giunti, una singolarità si verifica quando il braccio è completamente esteso o completamente ripiegato, perché in queste configurazioni il robot non è più in grado di muoversi lungo tutte le direzioni nel piano.

### Esempio: Braccio Robotico a 3 Giunti nello Spazio 3D

Consideriamo ora un braccio robotico a 3 giunti nello spazio tridimensionale. La posizione dell'end-effector è descritta dalle coordinate \\((x, y, z)\\) nello spazio 3D, e ogni giunto ruota attorno a un asse diverso.

Per un robot a 3 giunti, la Jacobiana sarà una matrice \\(3 \\times 3\\) che descrive la velocità lineare dell'end-effector in funzione delle velocità angolari dei giunti \\(\\theta_1\\), \\(\\theta_2\\), \\(\\theta_3\\).

\\[
J(\\theta) = \\begin{bmatrix}
\\frac{\\partial x}{\\partial \\theta_1} & \\frac{\\partial x}{\\partial \\theta_2} & \\frac{\\partial x}{\\partial \\theta_3} \\\\
\\frac{\\partial y}{\\partial \\theta_1} & \\frac{\\partial y}{\\partial \\theta_2} & \\frac{\\partial y}{\\partial \\theta_3} \\\\
\\frac{\\partial z}{\\partial \\theta_1} & \\frac{\\partial z}{\\partial \\theta_2} & \\frac{\\partial z}{\\partial \\theta_3}
\\end{bmatrix}
\\]

Questa Jacobiana consente di calcolare la velocità dell'end-effector e di analizzare le forze e i momenti torcenti sui giunti.

### Applicazioni della Jacobiana in Robotica

1. **Controllo dei Robot**: La Jacobiana viene utilizzata nei controllori robotici per convertire le velocità dei giunti in velocità dell'end-effector e viceversa.
   
2. **Analisi delle Forze**: È utilizzata per calcolare i momenti torcenti necessari nei giunti per sostenere le forze applicate all'end-effector.

3. **Cinematica Inversa**: La Jacobiana è importante per risolvere problemi di cinematica inversa, poiché può essere utilizzata per iterare verso soluzioni che soddisfano i requisiti di posizione e orientamento dell'end-effector.

4. **Singolarità**: Analizzare la Jacobiana aiuta a identificare configurazioni in cui il robot perde gradi di libertà (singolarità) e quindi a evitare queste configurazioni problematiche.

### Sintesi

La **matrice Jacobiana** è un concetto chiave in robotica, utilizzato per collegare le velocità dei giunti con le velocità dell'end-effector e per calcolare le forze e i momenti torcenti. La sua importanza si estende alla cinematica, al controllo dei robot e all'analisi delle singolarità.
"""
	load_text(text)


if DEBUG: Test()
else: main()

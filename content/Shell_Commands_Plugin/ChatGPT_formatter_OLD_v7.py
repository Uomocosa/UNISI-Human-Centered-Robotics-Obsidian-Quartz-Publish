

import win32clipboard
from markdownify import markdownify
import win32
import unicodedata
import re, sys
from dataclasses import dataclass


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

DEBUG = False # Remeber to set it to False

def main():
	text = get_text_from_clipboard()
	text = remove_new_lines_from_multiline_math_formulas(text)
	text = aggregate_multiline_math_formulas(text)
	lines = text.split('\n')
	# print(f"***text***:\n- {text}\n")

	# inside_title = False
	# inside_non_bullet_list = False
	indentation_level = 1
	# add_indentation_level = False
	# sub_indentation_level = False

	for line in lines:
		line = line.replace('\\(', '$')
		line = line.replace('\\)', '$')
		line = line.replace('\\[', '$$')
		line = line.replace('\\]', '$$')

		is_indented = search_for_indentation(line)		
		if is_indented: 
			# print(">>> (is_indented)")
			line = remove_indentation(line)
			# indentation_level += 1

		if not line: continue
		title = search_for_title(line)
		bullet_list = search_for_bullet_list(line)
		non_bullet_list = search_for_non_bullet_list(line)

		if title: 
			# print(">>> (title)")
			indentation_level = 2
			new_line = '\t'*(indentation_level-1) + f'- ***{title}***:\n'

		elif bullet_list:
			# print(">>> (bullet_list)")
			new_line = '\t'*(indentation_level+1) + f'- {bullet_list}\n'

		elif non_bullet_list:
			# print(">>> (non_bullet_list)")
			start = line.find('. ') + len('. ')
			line = line[:start] + line[start:].replace('. ', '.<br>')
			new_line = '\t'*(indentation_level) + f'  {line}\n'

		else:
			new_line = '\t'*indentation_level + f'- {line}\n'

		if not non_bullet_list: new_line = new_line.replace('. ', '.<br>')
		# print(new_line, end='')
		new_line = new_line.encode('utf-8')
		sys.stdout.buffer.write(new_line)


		# if is_indented: indentation_level -= 1
		# if add_indentation_level:
		# 	indentation_level += 1
		# 	add_indentation_level = False

		# if sub_indentation_level:
		# 	indentation_level -= 1
		# 	sub_indentation_level = False
	return





def Test(): 
	tests = [None, Test_1, Test_2]
	assert tests[2]()


def Test_1():
	load_text_1()
	main()
	return True

def Test_2():
	load_text_2()
	main()
	return True


def Test_formats():
	print(win32clipboard.CountClipboardFormats())
	print(win32clipboard.EnumClipboardFormats(0))
	print(win32clipboard.GetClipboardFormatName(49290))





def search_for_indentation(line):
	pattern = r'^( *)'
	matches = re.match(pattern, line)
	if not matches: return None
	indentation = len(matches.group(1))
	# print(f"INDENTATION = {indentation}")
	return indentation

def remove_indentation(line):
	return line.lstrip()


def search_for_title(line):
	pattern = r'^(#{1,6})\s+(.+)$'
	matches = list(re.finditer(pattern, line, re.MULTILINE))
	if not matches: return None
	title = matches[0].group(2)
	return title
	

def search_for_bullet_list(line):
	pattern = r'^[\*\-\+]\s+(.+)$'
	matches = re.match(pattern, line)
	# print(matches)
	if not matches: return None
	bullet_list = matches.group(1)
	# print(f"bullet_list = {bullet_list}")
	return bullet_list


def search_for_non_bullet_list(line):
	# Mening a numeric list, alphabetic list
	pattern = r'^([0-9]\.|^[a-zA-Z]\.)\s+(.+)$'
	matches = re.match(pattern, line)
	# print(matches)
	if not matches: return None
	non_bullet_list = matches.group(1)
	# print(f"non_bullet_list = {non_bullet_list}")
	return non_bullet_list



def remove_new_lines_from_multiline_math_formulas(text):
	pattern = r'\\\[(.*?)\\\]'
	matches = list(re.finditer(pattern, text, re.DOTALL))
	while(matches):
		match = matches[0]
		# print(match)
		start, end = match.span()
		sx = 5
		dx = 5
		k = 2 # len('\\['), len('//]')
		formula = text[start+k:end-k]
		# print(f"formula = '{formula}'")
		formula_with_context = text[start-sx:end+dx]
		# print(f"formula_with_context = '{formula_with_context}'")
		formula_without_new_lines = formula.replace('\n', '').lstrip().rstrip()
		# print(f"formula_without_new_lines = '{formula_without_new_lines}'")
		text = text[:start+k] + formula_without_new_lines + text[end-k:]
		# print(f"new_text = '{formula_without_new_lines}'")


		end = start + len(formula_without_new_lines) + k
		text_to_replace = text[start-sx:end+dx] # formula with context
		# print(f"text_to_replace = {text_to_replace}")

		text_to_replace = text_to_replace.replace('\n- \\[', '$$')
		text_to_replace = text_to_replace.replace('\n+ \\[', '$$')
		text_to_replace = text_to_replace.replace('\n* \\[', '$$')

		text_to_replace = text_to_replace.replace('\n   \\[', '$$')
		text_to_replace = text_to_replace.replace('\n  \\[', '$$')
		text_to_replace = text_to_replace.replace('\n \\[', '$$')
		text_to_replace = text_to_replace.replace('\n\\[', '$$')
		text_to_replace = text_to_replace.replace('\\]   \n', '$$')
		text_to_replace = text_to_replace.replace('\\]  \n', '$$')
		text_to_replace = text_to_replace.replace('\\] \n', '$$')
		text_to_replace = text_to_replace.replace('\\]\n', '$$')

		text_to_replace = text_to_replace.replace('   \\[', '$$')
		text_to_replace = text_to_replace.replace('  \\[', '$$')
		text_to_replace = text_to_replace.replace(' \\[', '$$')
		text_to_replace = text_to_replace.replace('\\[', '$$')
		text_to_replace = text_to_replace.replace('\\]   ', '$$')
		text_to_replace = text_to_replace.replace('\\]  ', '$$')
		text_to_replace = text_to_replace.replace('\\] ', '$$')
		text_to_replace = text_to_replace.replace('\\]', '$$')


		text_to_replace = text_to_replace.replace('- \\[', '$$')
		text_to_replace = text_to_replace.replace('+ \\[', '$$')
		text_to_replace = text_to_replace.replace('* \\[', '$$')

		# print(f"text_to_replace = '{text_to_replace}'")
		text = text[:start-sx] + text_to_replace + text[end+dx:]
		matches = list(re.finditer(pattern, text, re.DOTALL))
	return text



def aggregate_multiline_math_formulas(text):
	pattern = r'(\$\$(.*?)\$\$)'
	matches = list(re.finditer(pattern, text, re.DOTALL))

	splitted_text = list()
	formulas = list()
	k = 0
	for match in matches:
		start, end = match.span()
		splitted_text.append((k, start, text[k:start]))
		formulas.append(text[start:end])
		k = end


	text = ''
	formulas_to_combine = [None, None]
	indices_to_combine = list()
	allowed_chars = [' ', '\n', '\t', '\r']
	for i in range(len(splitted_text)):
		k = splitted_text[i][0]
		start = splitted_text[i][1]
		text_in_between_formulas = splitted_text[i][2]
		if i == 0 and start != 0: continue

		if formulas_to_combine[0]:
			# print(f"formulas_to_combine = {formulas_to_combine}")
			formulas_to_combine = [None, None]
			indices_to_combine.append(formulas_to_combine)

		if does_str_contains_only_these_chars(
			text_in_between_formulas, allowed_chars
		):
			if not formulas_to_combine[0]:
				formulas_to_combine[0] = i-1
				formulas_to_combine[1] = i
			else:
				formulas_to_combine[1] = i

	# for i, formula in enumerate(formulas): print(f"formula[{i}] = {formula}")
	for i, j in indices_to_combine[::-1]:
		for k in range(i,j): 
			print(f"k = {k}")
			del splitted_text[k+1]
		# print(f"i, j = {i, j}")
		# print(f"\tformulas[i:j] = {formulas[i:j+1]}")
		aggregated_formula = '$$\\begin{array}{l} '
		for k in range(i,j+1):
			# print(f"k = {k}")
			aggregated_formula += formulas[k][2:-2] + ' \\\\ '
		aggregated_formula = aggregated_formula[:-2] + ' \\end{array}$$'
		# print(f"\taggregated_formula = {aggregated_formula}")
		formulas[i] = aggregated_formula
		del formulas[j]
	# for i, formula in enumerate(formulas): print(f"formula[{i}] = {formula}")
	# print(f"len(splitted_text) = {len(splitted_text)}")

	text = ''
	for i in range(len(formulas)): 
		text += splitted_text[i][2] + formulas[i]

	return text


def does_str_contains_only_these_chars(string, allowed_chars):
    return all(char in allowed_chars for char in string)






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



def is_line_numeric_list(line):
	if type(line) is not str: return (False, -1)

	list_of_ignored_chars = ["", " ", "\t"]
	i = 0
	for index, char in enumerate(line):
		i += 1
		if char in list_of_ignored_chars: i-=1
		elif i > 3: return (False, -1)
		elif char == ".": return (True, index + 2)
	return (False, -1)



def add_brake_lines_after_a_point(line):
	is_line_numeric_list_, index = is_line_numeric_list(line)
	if is_line_numeric_list_: start = index
	else: start = 0

	output_line = line[:start]

	for i in range(start, len(line)):
		char_1 = line[i-1]
		char_2 = line[i]
		output_line += char_2
		if char_1 == "." and char_2 == " " :
			if len(line) >= i+5 and line[i+1:i+5] != "<br>": 
				output_line = output_line[:-1] + "<br>"

	return output_line




def format_numeric_line(line):
	for index, char in enumerate(line):
		if char == "\t": continue
		else: break
	if line[index:index+2] == "  ": return line + "\n"
	else: return "\t" + line[:index] + '  ' + line[index:] + "\n"




def get_text_from_clipboard():
	win32clipboard.OpenClipboard()
	if not is_ClipboradFormat_known(): return

	lines = get_lines_from_clipboard()
	# pretty_print_lines(lines)
	text = '\n'.join(lines)
	return text



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




def format_ChatGPT_output_in_Obsidian_format():
	markdown_str = ""

	chatgpt_format = POSSIBLE_CHATGPT_TEXT_FORMATS[0]
	for format_code in POSSIBLE_CHATGPT_TEXT_FORMATS:
		if win32clipboard.IsClipboardFormatAvailable(format_code):
			chatgpt_format = format_code
			break

	if win32clipboard.IsClipboardFormatAvailable(chatgpt_format):
		data = win32clipboard.GetClipboardData(chatgpt_format)
		markdown_str = markdownify(data, bullets='-')
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

	formatted_str = ""
	for line in markdown_str.split("\n"):
		line = line.replace("\r","")
		if len(line) == 0: continue


		line = add_brake_lines_after_a_point(line)

		_is_line_numeric_list, _ =  is_line_numeric_list(line)
		
		if _is_line_numeric_list: formatted_str += format_numeric_line(line)
		else:
			# print(line)
			formatted_str += "\t"
			if line[0] == "-": formatted_str += "\t"
			else: formatted_str += "- "
			formatted_str += line + "\n"

	formatted_str = formatted_str[3:-1]
	# win32clipboard.EmptyClipboard() #not needed
	# win32clipboard.SetClipboardText(formatted_str, FORMAT_2) #not needed
	win32clipboard.CloseClipboard()
	return formatted_str



def send_to_clipboard(clip_type, data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(clip_type, data)
	win32clipboard.CloseClipboard()





unicode2mathjax_dict = {
	"α" : "$\\alpha$",
	"β" : "$\\beta$",
	"ω" : "$\\omega$",
	"ρ" : "$\\rho$",
	"π" : "$\\pi$",
	"μ" : "$\\mu$",
	"λ" : "$\\lambda$",
	"η" : "$\\eta$",
	"δ" : "$\\delta$",
	"γ" : "$\\gamma$",
	"Ω" : "$\\Omega$",
	"Φ" : "$\\Phi$",
	"Σ" : "$\\Sigma$",
	"Π" : "$\\Pi$",
	"Θ" : "$\\Theta$",
	"Δ" : "$\\Delta$",
	"Γ" : "$\\Gamma$",
	"⌇" : "$(?)$",
	"⌆" : "$(?)$",
	"⌅" : "$(?)$",
	"⌀" : "$\\oslash$",
	"⋝" : "$(?)$",
	"⋜" : "$(?)$",
	"⋛" : "$(?)$",
	"⋚" : "$(?)$",
	"⊎" : "$(?)$",
	"≩" : "$(?)$",
	"≨" : "$(?)$",
	"≥" : "$\\meq$",
	"≤" : "$\\leq$",
	"∪" : "$\\cup$",
	"∩" : "$\\cap$",
	"∖" : "$\\$",
	"∕" : "$/$",
	"∓" : "$\\mp$",
	"−" : "$-$",
	"∅" : "$\\varnothing$",
	"∂" : "$\\partial$",
	"⁄" : "$/$",
	"=" : "=",
	"÷" : "$\\div$",
	"×" : "$\\times$",
	"±" : "$\\pm$",
	"𝛛" : "$\\mathbf{\\partial}$",
	"𝛚" : "$\\mathbf{\\omega}$",
	"𝛔" : "$\\mathbf{\\sigma}$",
	"𝛒" : "$\\mathbf{\rho}$",
	"𝛑" : "$\\mathbf{\\pi}$",
	"𝛍" : "$\\mathbf{\\mu}$",
	"𝛌" : "$\\mathbf{\\lambda}$",
	"𝛈" : "$\\mathbf{\\eta}$",
	"𝛅" : "$\\mathbf{\\delta}$",
	"𝛄" : "$\\mathbf{\\gamma}$",
	"𝛃" : "$\\mathbf{\\beta}$",
	"𝛂" : "$\\mathbf{\\alpha}$",
	"𝛀" : "$\\mathbf{\\Omega}$",
	"𝚽" : "$\\mathbf{\\Phi}$",
	"𝚺" : "$\\mathbf{\\Sigma}$",
	"𝚷" : "$\\mathbf{\\Pi}$",
	"𝚯" : "$\\mathbf{\\Theta}$",
	"𝚫" : "$\\mathbf{\\Delta}$",
	"𝚪" : "$\\mathbf{\\Gamma}$",
	"⩶" : "$===$",
	"⩵" : "$==$",
	"⩲" : "$(?)$",
	"⩐" : "$(?)$",
	"⩏" : "$(?)$",
	"⩎" : "$(?)$",
	"⩍" : "$(?)$",
	"⩌" : "$(?)$",
	"⩋" : "$(?)$",
	"⩊" : "$(?)$",
	"⩉" : "$(?)$",
	"⩈" : "$(?)$",
	"⩇" : "$(?)$",
	"⩆" : "$(?)$",
	"⩅" : "$(?)$",
	"⩄" : "$(?)$",
	"⩃" : "$(?)$",
	"⩂" : "$(?)$",
	"⩁" : "$(?)$",
	"⩀" : "$(?)$",
	"⨿" : "$(?)$",
	"⨻" : "$(?)$",
	"⨺" : "$(?)$",
	"⨹" : "$(?)$",
	"⨸" : "$(?)$",
	"⨷" : "$(?)$",
	"⨶" : "$(?)$",
	"⨵" : "$(?)$",
	"⨴" : "$(?)$",
	"⨳" : "$(?)$",
	"⨲" : "$(?)$",
	"⨱" : "$(?)$",
	"⨮" : "$(?)$",
	"⨭" : "$(?)$",
	"⨬" : "$(?)$",
	"⨫" : "$(?)$",
	"⨪" : "$(?)$",
	"⨩" : "$(?)$",
	"⨨" : "$(?)$",
	"⨧" : "$(?)$",
	"⨦" : "$(?)$",
	"⨥" : "$(?)$",
	"⨤" : "$(?)$",
	"⨣" : "$(?)$",
	"⨢" : "$(?)$",
	"⨝" : "$(?)$",
	"⨜" : "$(?)$",
	"⨛" : "$(?)$",
	"⨚" : "$(?)$",
	"⨙" : "$(?)$",
	"⨘" : "$(?)$",
	"⨗" : "$(?)$",
	"⨖" : "$(?)$",
	"⨕" : "$(?)$",
	"⨔" : "$(?)$",
	"⨓" : "$(?)$",
	"⨒" : "$(?)$",
	"⨑" : "$(?)$",
	"⨐" : "$(?)$",
	"⨏" : "$(?)$",
	"⨎" : "$(?)$",
	"⨍" : "$(?)$",
	"⨌" : "$\\iiint$",
	"⨋" : "$(?)$",
	"⨊" : "$(?)$",
	"⧻" : "$(?)$",
	"⧺" : "$(?)$",
	"⧁" : "$(?)$",
	"⧀" : "$(?)$",
	"⦼" : "$(?)$",
	"⦻" : "$(?)$",
	"⦺" : "$(?)$",
	"⦷" : "$(?)$",
	"⦰" : "$(?)$",
	"⦟" : "$(?)$",
	"⦝" : "$(?)$",
	"⦜" : "$(?)$",
	"⦀" : "$(?)$",
	"➗" : "$(?)$",
	"‰" : "$(?)$",
	"¬" : "$(?)$",
	"°" : "$°$",
	"±" : "$\\pm$",
	"µ" : "$\\mu$",
	"¼" : "$\\frac{1}{4}$",
	"½" : "$\\frac{1}{2}$",
	"¾" : "$\\frac{3}{4}$",
	"×" : "$\\times$",
	"Ø" : "$\\emptyset$",
	"÷" : "$\\div$",
	"¹" : "$^{1}$",
	"²" : "$^{2}$",
	"³" : "$^{3}$",
	"⁴" : "$^{4}$",
	"⁵" : "$^{5}$",
	"⁶" : "$^{6}$",
	"⁷" : "$^{7}$",
	"⁸" : "$^{8}$",
	"⁹" : "$^{9}$",
	"⁰" : "$^{0}$",
	"₁" : "$_{1}$",
	"₂" : "$_{2}$",
	"₃" : "$_{3}$",
	"₄" : "$_{4}$",
	"₅" : "$_{5}$",
	"₆" : "$_{6}$",
	"₇" : "$_{7}$",
	"₈" : "$_{8}$",
	"₉" : "$_{9}$",
	"₀" : "$_{0}$",
	"α" : "$\\alpha$",
	"β" : "$\\beta$",
	"γ" : "$\\gamma$",
	"δ" : "$\\delta$",
	"ε" : "$\\varepsilon$",
	"ζ" : "$\\zeta$",
	"η" : "$\\eta$",
	"θ" : "$\\theta$",
	"ι" : "$\\iota$",
	"κ" : "$\\kappa$",
	"λ" : "$\\lambda$",
	"μ" : "$\\mu$",
	"ν" : "$\\nu$",
	"ξ" : "$\\xi$",
	"ο" : "$o$",
	"π" : "$\\pi$",
	"ρ" : "$\\rho$",
	"σ" : "$\\sigma$",
	"τ" : "$\\tau$",
	"υ" : "$\\upsilon$",
	"φ" : "$\\phi$",
	"χ" : "$\\chi$",
	"ψ" : "$\\psi$",
	"ω" : "$\\omega$",
	"Α" : "$A$",
	"Β" : "$B$",
	"Γ" : "$\\Gamma$",
	"Δ" : "$\\Delta$",
	"Ε" : "$E$",
	"Ζ" : "$Z$",
	"Η" : "$H$",
	"Θ" : "$\\Theta$",
	"Ι" : "$I$",
	"Κ" : "$K$",
	"Λ" : "$\\Lambda$",
	"Μ" : "$M$",
	"Ν" : "$N$",
	"Ξ" : "$\\Xi$",
	"Ο" : "$O$",
	"Π" : "$\\Pi$",
	"Ρ" : "$P$",
	"Σ" : "$\\Sigma$",
	"Τ" : "$T$",
	"Υ" : "$Y$",
	"Φ" : "$\\Phi$",
	"Χ" : "$X$",
	"Ψ" : "$\\Psi$",
	"Ω" : "$\\Omega$",
	"ϑ" : "$\\vartheta$",
	"ϒ" : "$\\gamma$",
	"ϖ" : "$\\varpi$",
	"ϕ" : "$\\varphi$",
	"ϰ" : "$\\varkappa$",
	"ϱ" : "$\\varrho$",
	"ς" : "$\\varsigma$",
	"≡" : "$\\equiv$",
	"≈" : "$\\approx$",
	"≥" : "$\\leq$",
	"≤" : "$\\meq$",
	"√" : "$\\sqrt{}$",
	"∑" : "$\\sum$",
	"ⁿ" : "$^{n}$",
	"∞" : "$\\infty$",
	"⌠" : "$(?)$",
	"⌡" : "$(?)$",
	"∂" : "$\\partial$",
	"∆" : "$\\Delta$",
	"∏" : "$\\prod$",
	"∟" : "$(?)$",
	"⁺" : "$^{+}$",
	"⁻" : "$^{-}$",
	"⁼" : "$^{=}$",
	"⁽" : "$^{(}$",
	"⁾" : "$^{)}$",
	"ᶠ" : "$^{f}$",
	"ᶜ" : "$^{c}$",
	"ᵀ" : "$^{T}$",
	"₊" : "$_{+}$",
	"₋" : "$_{-}$",
	"₌" : "$_{=}$",
	"₍" : "$_{(}$",
	"₎" : "$_{)}$",
	"ₐ" : "$_{a}$",
	"ₑ" : "$_{e}$",
	"ₒ" : "$_{o}$",
	"ₓ" : "$_{x}$",
	"ₕ" : "$_{h}$",
	"ₖ" : "$_{k}$",
	"ₗ" : "$_{l}$",
	"ₘ" : "$_{m}$",
	"ₙ" : "$_{n}$",
	"ₚ" : "$_{p}$",
	"ₛ" : "$_{s}$",
	"ₜ" : "$_{t}$",
	"∇" : "$\\nabla$",
	"·" : "$\\cdot$",
	"è" : "è",
	"é" : "é",
	"$" : "$",
	"$$" : "$$",
	"’" : "'",
	"ò" : "o'",
	"à" : "à",
	"è" : "è",
	"\\(" : "$",
	"\\)" : "$",
	"\\[" : "$$",
	"\\]" : "$$",

	# TO ADD:
	#	× ÷ ± ∓ √ ∛ ∜ ∞ ∑ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵
	# 	½ ⅓ ⅔ ¼ ¾ ⅛ ⅜ ⅝ ⅞ ⅟
	#	¢ € £ ¥ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ ₭ ₮ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ₶ ₷ ₸ ₹
	# 	%
	# 	© ® ™ ° ‰ § ¶ † ‡ • ª º № ¿ ¡
}


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

Questo processo continua per ogni passo temporale. Il Metodo di Eulero approssima quindi l'andamento dell'oscillatore armonico nel tempo.

### Limiti del Metodo di Eulero

- **Precisione**: Il Metodo di Eulero è relativamente semplice e veloce, ma non è molto preciso, soprattutto se il passo temporale \\(\\Delta t\\) è troppo grande. Errori di approssimazione si accumulano rapidamente.
  
- **Stabilità**: Per alcuni sistemi dinamici, come quelli con oscillazioni rapide (ad esempio l'oscillatore armonico), il metodo può essere instabile se \\(\\Delta t\\) non è abbastanza piccolo.

Per risolvere problemi più complessi con maggiore precisione, si utilizzano metodi numerici più avanzati, come il **Metodo di Eulero Modificato** (o metodo del punto medio) o i metodi **Runge-Kutta**.

Spero che questo chiarisca il concetto di Metodo di Eulero e come viene applicato nella risoluzione numerica di equazioni differenziali!
"""
	load_text(text)

if DEBUG: Test()
else: main()

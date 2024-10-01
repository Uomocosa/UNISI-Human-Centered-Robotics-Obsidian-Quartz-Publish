

import win32clipboard
from markdownify import markdownify
import win32


win32clipboard.OpenClipboard()
# print(win32clipboard.CountClipboardFormats())
# print(win32clipboard.EnumClipboardFormats(0))
# print(win32clipboard.GetClipboardFormatName(49290))

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
	print(formatted_str, end="")
	# win32clipboard.EmptyClipboard() #not needed
	# win32clipboard.SetClipboardText(formatted_str, FORMAT_2) #not needed
	win32clipboard.CloseClipboard()

# if __name__ == "__main__": format_ChatGPT_output_in_Obsidian_format()
format_ChatGPT_output_in_Obsidian_format()
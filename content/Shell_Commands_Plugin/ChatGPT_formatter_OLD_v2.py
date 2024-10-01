

import win32clipboard
from markdownify import markdownify
import win32
import unicodedata


# ₁
# ∇∇∇∇∇∇∇∇
""" 
#TODO (or not)
format_equation_rules = [
	# An "equation" is a substring that:
	# 	starts with "$" and end with "$" (inline equation)
	# 	or starts with "$$" and end with "$$" (equation)

	# Numbers are always considerated as an equation or parts of one,
	# but they do not begin with "$", same with signs : "-", "+", "*", "^", ecc.

	# If two distinct INLINE equations are concatenated, join them
	#	~Ex.: $\alpha$$\beta$ must become $\alpha\beta$
	#	~Ex.: $\alpha$ $\beta$ must become $\alpha \beta$
]
"""

def main():
	win32clipboard.OpenClipboard()

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

	formatted_str = format_ChatGPT_output_in_Obsidian_format()
	# print(formatted_str, end="")

	for key, item in unicode2mathjax_dict.items():
		formatted_str = formatted_str.replace(key, item)
		
	is_okay_to_print_formatted_str = True
	list_of_symbols_to_be_added = []
	encoded_str = formatted_str.encode('utf-8')
	for i, char in enumerate(formatted_str):
		encoded_char = str(char.encode('utf-8'))[2:-1]
		if encoded_char == "\\n": continue
		if encoded_char == "\\t": continue
		if encoded_char == "\\\\": continue
		if char in unicode2mathjax_dict.keys(): continue
		if encoded_char != char:
			is_okay_to_print_formatted_str = False
			if char not in list_of_symbols_to_be_added:
					list_of_symbols_to_be_added.append(char)

	symbols_needed_to_be_add_to_this_script = ""
	# print(list_of_symbols_to_be_added)
	for symbol in list_of_symbols_to_be_added:
		# print(symbol)
		symbols_needed_to_be_add_to_this_script += f'\t"{symbol}" : "$$",\n'
	symbols_needed_to_be_add_to_this_script = symbols_needed_to_be_add_to_this_script[1:]

	if is_okay_to_print_formatted_str: print(formatted_str, end="")
	else: 
		# [13, 49802, 16, 1, 7]
		clip_type = 13
		data = symbols_needed_to_be_add_to_this_script
		send_to_clipboard(clip_type, data)
		err_msg = "Some character cannot be printed "
		err_msg += "(problems with Shell Command Plugins)<br>"
		err_msg += "They have been saved to the Clipboard<br>" 
		err_msg += "Please add them in the script 'ChatGPT_formatter.py'" 
		print(err_msg)




def Test_formats():
	print(win32clipboard.CountClipboardFormats())
	print(win32clipboard.EnumClipboardFormats(0))
	print(win32clipboard.GetClipboardFormatName(49290))



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
	# win32clipboard.EmptyClipboard() #not needed
	# win32clipboard.SetClipboardText(formatted_str, FORMAT_2) #not needed
	win32clipboard.CloseClipboard()
	return formatted_str







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






def send_to_clipboard(clip_type, data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(clip_type, data)
	win32clipboard.CloseClipboard()


main()
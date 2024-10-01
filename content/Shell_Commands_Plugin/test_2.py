import re

# Regular expression to find strictly consecutive math blocks
pattern = r'(\$\$(.*?)\$\$\s*){2,}'
pattern = r'\$\$.*?\$\$\s*(?=\$\$)'

# Example text with consecutive math blocks and non-math content
text = """
$$
multi-line equation (1)
$$
Some more text.
$$
multi-line equation (2)
$$
$$
multi-line equation (3)
$$
"""

# Find strictly consecutive math blocks
matches = re.finditer(pattern, text, re.DOTALL)

# Print each consecutive match and its indices
for match in matches:
    consecutive_math_blocks = match.group(0)  # The entire consecutive math block match
    start_index, end_index = match.span()  # Start and end indices of the match
    print(f"Consecutive math blocks:\n{consecutive_math_blocks.strip()}")
    print(f"Start index: {start_index}, End index: {end_index}")

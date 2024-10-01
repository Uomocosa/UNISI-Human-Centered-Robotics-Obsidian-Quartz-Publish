import re

# Regex pattern
pattern = r"(?<!\d)\. [^\n]"

# Example text
text = """
1. This is a numbered list.
99. Here's another list item.
This is a regular sentence. And here is another one.
This one has a period. Right before more text.
"""

# Finding all matches
matches = re.findall(pattern, text)

# Output matches
print(matches)

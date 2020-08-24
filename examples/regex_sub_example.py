# Using the regex sub() method to find and replace
import re

# Using sub() method to find and replace secret agent names
# secretText = 'Agent Alice gave the secret document to Agent Bob.'
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.findall(secretText))
# print(namesRegex.sub('REDACTED', secretText))

# Using sub() method and '\1' to truncate secret agent names with just the text in group 1
# secretText = 'Agent Alice gave the secret document to Agent Bob.'
# namesRegex = re.compile(r'Agent (\w)\w*') # note that group 1 is first letter in agent name
# print(namesRegex.findall(secretText))
# print(namesRegex.sub(r'Agent \1****', secretText))

# Using re.VERBOSE to ignore spaces and comments for better inline documentation
re.compile(r'''
(\d\d\d-)|  # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash
\d\d\d      # first three digits
-           # second dash
\d\d\d\d    # last 4 digits
''', re.VERBOSE)

# Note: use re.IGNORECASE to match case insensitive
# or re.DOTALL to match anything (incl. newlines) with '.'
# Use bitwise operator '|' to pass multiple arguments to re.compile()

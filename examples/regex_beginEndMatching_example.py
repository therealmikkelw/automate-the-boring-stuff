import re

# Using '^' character to match only strings beginning with some regex expression
# beginsWithHelloRegex = re.compile(r'^Hello')

# Using '$' character to match only strings ending with some regex expression
# endsWithWorldRegex = re.compile(r'world!$')

# Using '^' and '$' to match entire string (both beginning and end of string)
# allDigitsRegex = re.compile(r'^\d+$')
# mo = allDigitsRegex.search('14289235080435')
# print(mo.group())

# Using '.' wildcard character to match anything but newlines
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Using '.*' to match Anything (but newlines)
# name = 'First Name: Mikkel Last Name: Hestepik'
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# print(nameRegex.findall(name))

# Example of non-greedy matching using '.*' and '?'
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


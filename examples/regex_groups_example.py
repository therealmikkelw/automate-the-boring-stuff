import re

# finding regex groups using parenteheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print(mo.group(1))

# finding parentheses using the escape character '\'
# phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is (415) 555-4242')
# print(mo.group())

# finding variants of the same pattern using the pipe character '|'
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# Note: the group() method returns both a match and a span object

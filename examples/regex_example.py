import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # use raw string (r'') because RegEx use many backslashes
print(phoneNumRegex.findall(message)) # findall method returns all occurrences
# mo = phoneNumRegex.search(message) # search method returns first occurrence into a match object
# print(mo.group()) # match object can be accessed using group method


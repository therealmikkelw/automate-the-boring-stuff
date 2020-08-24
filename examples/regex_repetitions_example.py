import re 

# Using the ()? syntax if part of the pattern is optional
# The '?' character means match 'zero or one' times 
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The adventures of Batwoman')
# print(mo.group())

# Finding phone number with optional area code using ()?
# phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My phone number is 415-555-4242. Call me tomorrow.')
# print(mo.group())
                    
# The asterisk '*' character means match 'zero or more' times
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The adventures of Batwowowowoman')
# print(mo.group())

# The plus '+' character means match 'one or more' times (not optional)
# batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The adventures of Batman')
# print(mo.group())

# The {x} syntax means match exactly x times
# haRegex = re.compile(r'(Ha){3}')
# mo = haRegex.search('He laughed "HaHaHa".')
# print(mo.group())

# Finding three phone numbers using {x} syntax
# Optional area code, optional ',' separator
# phoneNumRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# mo = phoneNumRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
# print(mo.group())

# The {x,y} syntax means match at least x, at most y times (a range)
# Note: similar to slices, { ,y} or {x, } can be used
# haRegex = re.compile(r'(Ha){3,5}')
# mo = haRegex.search('He laughed "HaHaHaHaHa".')
# print(mo.group())

# Finding the first 3 to 5 digits using {x,y} syntax
# Note: Python returns '12345' because it uses greedy matching per default (the longest string possible)
# digitRegex = re.compile(r'(\d){3,5}')
# mo = digitRegex.search('1234567890')
# print(mo.group())

# Example of non-greedy matching using {x,y}? syntax
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())

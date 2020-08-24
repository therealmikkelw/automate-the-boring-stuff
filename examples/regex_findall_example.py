# The findall() method for regular expressions objects
import re

# findall() on regex with zero or one group
# returns a list of strings, not a match object like the search() method
# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumbers = phoneRegex.findall('Call 415-555-1212, 415-555-1234 or 505-555-9886')
# print(phoneNumbers)

# findall() on regex with two or more groups
# returns a list of tuples of strings (no. of strings acc. no. of groups)
# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# phoneNumbers = phoneRegex.findall('Call 415-555-1212, 415-555-1234 or 505-555-9886')
# print(phoneNumbers)

# Shorthand codes for character classes
# \d : numeric digits from 0 to 9
# \D : character that is NOT a numeric digit from 0 to 9
# \w : letter, numeric digit, or underscore
# \W : character that is not a letter, numeric digit, ot underscore
# \s : space, tab, or newline
# \S : character that is not a space, tab, or newline

# 12 days of Christmas example
# lyrics = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree'
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall(lyrics))

# Create your own character class using [] syntax
# doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# print(doubleVowelRegex.findall('Robocop eats baby food.'))

# Negative character classes using the ^ symbol
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food.'))

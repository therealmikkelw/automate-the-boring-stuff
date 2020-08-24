#! python3

import re, pyperclip

# Create regex object for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext., x12345

(
((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)      # first separator
\d\d\d      # first 3 digits
-           # second separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)   # extension word-part (optional)
 (\d{2,5}))?        # extension number-part (optional)
)
''', re.VERBOSE)

    
# Create regex object for email adresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+ # name part
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()


# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# print(extractedPhone)
# print(extractedEmail)


# Extract first string from each tuple in the list of tuples in extractedPhone
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)


# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



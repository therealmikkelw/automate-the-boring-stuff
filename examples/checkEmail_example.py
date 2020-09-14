import imapclient

# Create connection object (IMAP)
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# Log in to IMAP server
# Note: look up Google 'app specific password', which is different from the global Google password
conn.login( 'username' , 'password' )

# Select folder in mail account in read-only mode
conn.select_folder('INBOX', readonly=True)

# Using IMAP formatting (a list of strings), search for mails
# Note: return value is UIDs of all mails fulfilling criteria
# Note: other search keys include BEFORE date, ON date, SUBJECT string, BODY string, TEXT string, etc
# - see table 16.3 on automatetheboringstuff.com
UIDs = conn.search(['SINCE 20-Aug-2020'])

# Using IMAP formatting to fetch mail content from a UID (here 47474)
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS']))


# The pyzmail module is used to parse rawMessage to more readable format
# Could not install pyzmail module using pip install
import pyzmail

# Using pyzmail module to parse body of a particular email
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

# Get subject and from (or to) address
print(message.getSubject())
print(message.get_addresses('from')[1])

# Using text_part member variable to see if email has a plain text part
# if not, return value will be None
# Note: assuming UTF-8 string encoding
message.text_part
message.text_part.get_payload().decode('UTF-8')

# Using html_part member variable to see if email has a html part
message.html_part

# Log out from IMAP server
conn.logout()

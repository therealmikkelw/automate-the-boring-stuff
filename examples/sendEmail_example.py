import smtplib

# Create connection object (SMTP)
conn = smtplib.SMTP('smtp.gmail.com', 587)

# Using ehlo() method to start the connection
# Note: return code in the two hundreds means OK
conn.ehlo()

# Start TLS encryption (for sending password online)
# Note: return code in the two hundreds means OK
conn.starttls()

# Log in to SMPT server
# Note: look up Google 'app specific password', which is different from the global Google password
conn.login( 'username' , 'password' )

# Send emails
# Note: return value is a dictionary of all mails that failed to send - a blank dictionary means success
conn.sendmail( 'from-address', 'to-address',  'Subject: So long...\n\nDear Al,\n So long and thanks for all the fish.\n\n-Al')

# Disconnect from SMTP server
conn.quit()

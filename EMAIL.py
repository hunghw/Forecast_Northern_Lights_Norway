# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

with open('textfile') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'TEST'
msg['From'] = 'hungwh17@uia.no'
msg['To'] = 'hwhung0111@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('127.0.0.1')
s.send_message(msg)
s.quit()
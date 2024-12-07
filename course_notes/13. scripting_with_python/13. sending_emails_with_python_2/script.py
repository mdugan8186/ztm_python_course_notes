# ==== sending emails with python 2 ====

import smtplib
from email.message import EmailMessage

# email object
email = EmailMessage()
# who is the email from
email['from'] = 'Dugan'
# who is the email to
email['to'] = 'mdugan8186@gmail.com'
# the email subject line
email['subject'] = 'You won 1,000,000 dollars!'
# content of the email
email.set_content('I am a Python Master')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mdugan8187@gmail.com', '**** **** **** ****')
    smtp.send_message(email)
    print('all good')

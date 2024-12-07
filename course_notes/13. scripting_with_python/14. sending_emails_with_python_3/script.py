# ==== sending emails with python 3 ====

# use this this path
# michaeldugan@Michaels-MacBook-Pro ztm_python_course_notes % cd course_notes/13.\ scripting_with_python/14.\ sending_emails_with_python_3

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dugan'
email['to'] = 'mdugan8186@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mdugan8187@gmail.com', '**** **** **** ****')
    smtp.send_message(email)
    print('all good')

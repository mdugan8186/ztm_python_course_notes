# ==== sending emails with python ====

# simple mail transfer protocol
# smtp allows us to create a smtp server. anytime you send emails to anyone you need to have a server that communicates the language  of the email. emails have their own protocol for communicating like websites have http or https
import smtplib
from email.message import EmailMessage

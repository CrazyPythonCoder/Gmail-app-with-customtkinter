# import smtplib
# import os
#
# SENDER_EMAIL = 'aaravsonaniatpython@gmail.com'
# SENDER_PASSWORD = 'ayyvhlokzsrqnqam'
#
# USER = 'smartboybeingbe@gmail.com'
#
# # Normal Email with subject and password
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#
#     subject = 'Important'
#     body = 'How about dinner at 6pm this Saturday?'
#
#     msg = f'Subject: {subject}\n\n{body}'
#
#     smtp.sendmail(SENDER_EMAIL, USER, msg)

#################################################### ANOTHER GMAIL #################################################################

# import smtplib
# from email.message import EmailMessage
#
# SENDER_ADDRESS = 'aaravsonaniatpython@gmail.com'
# PASSWORD = 'ayyvhlokzsrqnqam'
#
# msg = EmailMessage()
# msg['Subject'] = 'This is another method'
# msg['From'] = SENDER_ADDRESS
# msg['To'] = 'smartboybeingbe@gmail.com'
# msg.set_content('New Method')
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(SENDER_ADDRESS, PASSWORD)
#     smtp.send_message(msg)


# ------------------------------------------- Attachment --------------------------------

# import smtplib
# from email.message import EmailMessage
# import imghdr
#
# SENDER_ADDRESS = 'aaravsonaniatpython@gmail.com'
# PASSWORD = 'ayyvhlokzsrqnqam'
#
# msg = EmailMessage()
# msg['Subject'] = 'This is new2'
# msg['From'] = SENDER_ADDRESS
# msg['To'] = 'smartboybeingbe@gmail.com'
# msg.set_content('New message with file attached')
#
# with open('img.jpg', 'rb') as file:
#     file_data = file.read()
#     file_type = imghdr.what(file.name)
#     file_name = file.name
#
# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(SENDER_ADDRESS, PASSWORD)
#     smtp.send_message(msg)


# import smtplib
# from email.message import EmailMessage
#
# SENDER_ADDRESS = 'aaravsonaniatpython@gmail.com'
# PASSWORD = 'ayyvhlokzsrqnqam'
#
# msg = EmailMessage()
# msg['Subject'] = 'This is new2'
# msg['From'] = SENDER_ADDRESS
# msg['To'] = 'smartboybeingbe@gmail.com'
# msg.set_content('New message with file attached')
#
# with open('test.py', 'rb') as file:
#     file_data = file.read()
#     file_name = file.name
#
# msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(SENDER_ADDRESS, PASSWORD)
#     smtp.send_message(msg)


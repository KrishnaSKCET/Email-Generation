
import csv,os
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


def sendEMail(csv_file, content):

    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contacts.append(row['Email'])
            names.append(row['Name'])

    count = 0

    for email in contacts:

        msg = EmailMessage()
        msg['Subject'] = 'Hello ' + names[count]
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email

        msg.set_content(content)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Sent mail to " + names[count] + " with email address " + email)
        count = count + 1
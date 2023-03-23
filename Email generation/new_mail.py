
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject='Greetings from Fresh Spar Technologies  '
    body='Hey Everybody, This is a testing message for our further training programs. Be updated in our website www.freshspar.com and Social Medias'
    msg=f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS,['727721eucb01@skcet.ac.in',

'727721eucb02@skcet.ac.in',

'727721eucb03@skcet.ac.in',

'727721eucb04@skcet.ac.in',

'727721eucb05@skcet.ac.in',

'727721eucb06@skcet.ac.in',

'727721eucb07@skcet.ac.in',

'727721eucb08@skcet.ac.in',

'727721eucb09@skcet.ac.in',

'727721eucb010@skcet.ac.in',

'727721eucb011@skcet.ac.in',

'727721eucb012@skcet.ac.in',

'727721eucb013@skcet.ac.in',

'727721eucb014@skcet.ac.in',

'727721eucb015@skcet.ac.in',

'727721eucb016@skcet.ac.in',

'727721eucb017@skcet.ac.in',

'727721eucb018@skcet.ac.in',

'727721eucb019@skcet.ac.in',

'727721eucb020@skcet.ac.in',

'727721eucb021@skcet.ac.in',

'727721eucb022@skcet.ac.in',

'727721eucb023@skcet.ac.in',

'727721eucb024@skcet.ac.in',

'727721eucb025@skcet.ac.in',

'727721eucb026@skcet.ac.in',

'727721eucb027@skcet.ac.in',

'727721eucb028@skcet.ac.in',

'727721eucb029@skcet.ac.in',

'727721eucb030@skcet.ac.in',

'727721eucb031@skcet.ac.in',

'727721eucb032@skcet.ac.in',

'727721eucb033@skcet.ac.in',

'727721eucb034@skcet.ac.in',

'727721eucb035@skcet.ac.in',

'727721eucb036@skcet.ac.in',

'727721eucb037@skcet.ac.in',

'727721eucb038@skcet.ac.in',

'727721eucb039@skcet.ac.in',

'727721eucb040@skcet.ac.in',

'727721eucb041@skcet.ac.in',

'727721eucb042@skcet.ac.in',

'727721eucb043@skcet.ac.in',

'727721eucb044@skcet.ac.in',

'727721eucb045@skcet.ac.in',

'727721eucb046@skcet.ac.in',

'727721eucb047@skcet.ac.in',

'727721eucb048@skcet.ac.in',

'727721eucb049@skcet.ac.in',

'727721eucb050@skcet.ac.in',

'727721eucb051@skcet.ac.in',

'727721eucb052@skcet.ac.in',

'727721eucb053@skcet.ac.in',

'727721eucb054@skcet.ac.in',

'727721eucb055@skcet.ac.in',

'727721eucb056@skcet.ac.in',

'727721eucb057@skcet.ac.in',

'727721eucb058@skcet.ac.in',

'727721eucb059@skcet.ac.in',

'727721eucb060@skcet.ac.in',

'727722eucb501@skcet.ac.in',

'727722eucb502@skcet.ac.in',

'727722eucb503@skcet.ac.in',

'727722eucb504@skcet.ac.in',

'727722eucb505@skcet.ac.in',

'727722eucb506@skcet.ac.in'],msg)
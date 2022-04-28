# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need


def send_email(to, msg_text):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('zy.sara93@gmail.com', 'ZYsaraZY')

    server.sendmail('zy.sara93@gmail.com',to,msg_text)
    server.quit()



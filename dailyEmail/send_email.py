from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from datetime import date


def send_email(html: str, from_mail: str, to_mail: str, password):
    # Create message container - the correct MIME type is multipart/alternative
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Today schedule {date.today().strftime('%B %d, %Y')}"
    msg['from_mail'] = from_mail
    msg['To'] = to_mail
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    # Send the message via local SMTP server.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_mail, password)

    # send email
    server.sendmail(from_mail, to_mail, msg.as_string())
    server.quit()

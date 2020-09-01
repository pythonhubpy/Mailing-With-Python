import smtplib
import dotenv
import os

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv('.env')

server = smtplib.SMTP('smtp.gmail.com', 25)

server.starttls()

server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

mail = MIMEMultipart()

mail['From'] = "Python Hub"
mail['To'] = "vetrichelvaninovator@gmail.com"
mail['Subject'] = 'This is a test message'

mail.attach(MIMEText("This a test mail sent with python by pythonhub.", 'plain'))

image = open('image.jpg', 'rb')
# audio = open('sample.mp3', 'rb') // Send Audio

attachment = MIMEBase('application', 'octet-stream')


attachment.set_payload(image.read())
# attachment.set_payload(audio.read()) // Send Audio

encoders.encode_base64(attachment)

attachment.add_header('Content-Disposition',
                      'attachment; filename=image.jpg')

# attachment.add_header('Content-Disposition',
#   'attachment; filename=sample.mp3') // Send Audio

mail.attach(attachment)

message = mail.as_string()

server.sendmail(os.getenv('EMAIL'), os.getenv('TO'), message)

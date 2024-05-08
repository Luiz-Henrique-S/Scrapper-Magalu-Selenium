import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#função para enviar email recebendo como paremetro o email do destinatario, o assunto, o corpo do email e o caminho do anexo
def enviar_email(email_destinatario, assunto, corpo, anexo_path):
    email_remetente = "luiz2562@gmail.com"
    senha_remetente = "phaj egpk gxpx ficm"
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    msg = MIMEMultipart()

    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    if anexo_path:
        attachment = open(anexo_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + anexo_path)
        msg.attach(part)

    server = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    server.starttls()

    server.login(email_remetente, senha_remetente)

    server.sendmail(email_remetente, email_destinatario, msg.as_string())

    server.quit()
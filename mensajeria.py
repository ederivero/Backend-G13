# MIME > Multipupose Internet Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# SMTP > Simple Mail Transfer Protocol
from smtplib import SMTP
from validate_email import validate_email
from os import environ

def cambiarPassword(destinatario):
    existeEmail = validate_email(destinatario)

    if not existeEmail:
        print('El correo no existe')
        return 
    
    texto = '''Hola
    Parece que has cambiado tu contraseña, si no fuiste tu comunicate con nosotros, caso contrario, has caso omiso a este mensaje'''
    emailEmisor = environ.get('CORREO_EMISOR') 
    passwordEmisor = environ.get('PASSWORD_CORREO_EMISOR')

    cuerpo = MIMEText(texto, 'plain') 

    correo = MIMEMultipart()
    # configuramos el titulo del correo
    correo['Subject'] = 'Cambiaste tu contraseña'

    # configuramos el destinatario del correo
    correo['To'] = destinatario

    # aca adjuntamos el cuerpo del correo
    correo.attach(cuerpo)

    #                   SERVIDOR      | PUERTO
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 587
    emisor = SMTP('smtp.gmail.com',587)

    emisor.starttls()

    # inicio sesion con mis credenciales
    emisor.login(emailEmisor, passwordEmisor)

    # enviamos el correo
    emisor.sendmail(from_addr=emailEmisor, to_addrs=destinatario, msg=correo.as_string())

    emisor.quit()

    print('Correo enviado exitosamente')
import ssl
from email.message import EmailMessage
#Protocolo simple de transferencia de correo
import smtplib

emisor_email = input('Escribe tu email:')
pasword_email = input('Escribe tu token generado en email:')
#en el receptor pondremos una lista de correos
receptor_email =[]
print("para separar los emails use un espacio:")
añadir_email = input("añadir emali:")

for i in añadir_email.split(" "):
    receptor_email.append(i)

asunto = input("Escribe el asunto: ")
cuerpo = input("Escribe tu mensaje: ")

em = EmailMessage()


#Usamos estos valores a las claves From y To del mensaje.
em['From'] = emisor_email
em['To'] = receptor_email
em['Subject'] = asunto
em.set_content(cuerpo)

#podremos utilisar el certificado de ssl
#contexto = ssl.create_default_contex()
contexto = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)


for i in receptor_email:
#en esta parte señalamos el servidor y el puerto
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
#en esta parte ponemos el usuario y contraseña para logearnos

        smtp.login(emisor_email, pasword_email)
#
        smtp.sendmail(emisor_email, i, em.as_string(contexto))
        print ('enviado...')

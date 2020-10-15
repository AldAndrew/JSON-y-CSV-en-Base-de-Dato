import smtplib, ssl

from email.mime.text import MIMEText 

def send_email(receptor,subject,msg):
    port = 465  # For SSL
    password = "xxxxx" #Corresponde a la contraseña de la cuenta de email

    # Create a secure SSL context
    context = ssl.create_default_context()

    emisor = "darkciberHuerfa@gmail.com"  #Cuenta de email

    mensaje = MIMEText(msg) 
    mensaje['From']=emisor 
    mensaje['To']=receptor 
    mensaje['Subject']=subject

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(emisor, password)
        server.sendmail(emisor,receptor,mensaje.as_string()) 
        server.close()
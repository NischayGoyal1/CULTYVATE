import email
import smtplib
from email.message import EmailMessage



EMAIL="swapswapy123@gmail.com"
PASS="4851Abce" 

def send_email(email,Nischay):
   with open("static/css/s.css","r") as f:
      data=f.read()

   msg=EmailMessage()
   msg["Subject"]="Verifcation"
   msg["from"]=EMAIL
   msg["to"]=email
   msg.set_content(f"""

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
         
         {data}
      </style>
   </head>
   <body>
      <div class="main">
      <h2 class="main-head">AGROLENDERS</h2>
      <div class="content">
         <h2>Hi there, {Nischay}!</h2>
         <p>Cultyvate<br>

Hey there vedant
Thank you for registering with us. Now you can start using our services like crop prediction, crop disease detection and fertilizer recommendation in order to increase your yield and maximize your profit.
<br>
Thank you team cultyvate</p>
         <br>
         <P>Cultyvate- farming made easy.</P>
      </div>
   </div>
   </body>
   </html>
   """,subtype="html")


   with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
      
      smtp.login(EMAIL,PASS)
      smtp.send_message(msg)
send_email("goyalivuq1@gmail.com","vedant")
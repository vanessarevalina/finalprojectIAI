import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 

print("Masukkan email dan password Anda")
sender_address = input("Email:")
sender_pass = input("Password:")

with open("/Users/vanessarevalina/Downloads/Documents/NESSA/IAI PYTHON/finalproject", 'r') as f:
    ff = f.read()
listreceiver = ff.split("\n")

loop = True
while loop:
   print ('-------------------------')
   print ("Apakah ingin mengirim email dengan file?")
   print ("0. Tidak\n1. Ya")
   jwb = input ("Masukkan kode input:")
   print ('-------------------------')

   if jwb == '1': 
      print ("\nMasukkan Subject dan Isi Email")
      inputsubject= input("Subject:")
      inputisi = input("Isi:")
      inputfile = input ("Input file path: ")

      for i in range(len(listreceiver)): 
         x = listreceiver[i]
         reciver_mail = x   
         print(reciver_mail)
         
         message = MIMEMultipart()
         message['From'] = sender_address
         message['To'] =  reciver_mail 
         message['Subject'] =  inputsubject    
         mail_content = inputisi
         
         message.attach(MIMEText(mail_content, 'plain'))
         filename = inputfile

         with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            
         encoders.encode_base64(part) 

         part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

         message.attach(part)
         s = smtplib.SMTP('smtp.gmail.com', 587) 
         s.starttls() 
         s.login(sender_address, sender_pass) 
         text = message.as_string()
         s.sendmail(sender_address, reciver_mail, text) 
         s.quit() 
         
         print('Mail Sent')
      loop = False
   
   elif jwb == '0':
      print ("\nMasukkan Subject dan Isi Email")
      inputsubject= input("Subject:")
      inputisi = input("Isi:")

      for i in range(len(listreceiver)): 
         x = listreceiver[i]
         reciver_mail = x   
         print(reciver_mail)
         
         message = MIMEMultipart()
         message['From'] = sender_address
         message['To'] =  reciver_mail 
         
         message['Subject'] =  inputsubject    
         mail_content = inputisi

         s = smtplib.SMTP('smtp.gmail.com', 587) 
         s.starttls() 
         s.login(sender_address, sender_pass) 
         text = message.as_string()
         s.sendmail(sender_address, reciver_mail, text) 
         s.quit() 

         print('Mail Sent')
      loop = False

   else: 
      print("KODE INPUT SALAH. MOHON MASUKKAN LAGI KODE INPUT") 
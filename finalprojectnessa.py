import smtplib 
import getpass

gmail_pengirim = input(str("Masukkan akun gmail pengirim : "))
password_gmail_pengirim = getpass.getpass("Masukkan password gmail pengirim : ")

#open file yang isinya email email yang mau kita kirim
with open('receiver_list.txt', 'r') as file:
	penerima = file.read().replace('\n', ',')

sent_from = gmail_pengirim
sent_to = penerima
sent_subject = input(str("SUBJEK : "))
sent_body = input(str("ISI : "))

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_pengirim, password_gmail_pengirim)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email terkirim yay!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
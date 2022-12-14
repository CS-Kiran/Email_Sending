import emails
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#(220, b'2.0.0 Ready to start TLS')
s.login("kiran2002bp@gmail.com", "uqatmwfbwhbzoxly")
#(235, b'2.7.0 Accepted')
message = "Sending Email 3 using Python Successfully"
s.sendmail("kiran2002bp@gmail.com", "kiran1007patil@gmail.com", message)
#{}
s.quit()
#(221, b'2.0.0 closing connection n9-20020a17090a670900b002190eabb890sm6357870pjj.25 - gsmtp')

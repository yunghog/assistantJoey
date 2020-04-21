#send an email
#author : Samartha
import smtplib as e
s=e.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("samarthahm@gmail.com","wwe9481504454")
message='from joey tribbiani'
s.sendmail("samarthahm@gmail.com","samarthaog@gmail.com",message)
s.quit()

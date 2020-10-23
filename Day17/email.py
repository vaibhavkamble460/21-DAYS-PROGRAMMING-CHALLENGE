import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

s.login("viabhav12@gmail.com","Kamble@123")
message="You have Selected as a campus director"

s.sendmail("viabhav12@gmail.com","abhishek.r.9690@gmail.com",message )

s.quit()
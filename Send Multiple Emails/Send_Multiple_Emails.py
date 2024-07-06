import smtplib as s

ob = s.SMPT('smtp.gmail.com', 587) #server and port number
ob.ehlo() #connector
ob.starttls() #sever connection

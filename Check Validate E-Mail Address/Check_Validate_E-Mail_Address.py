userEmail = input(" Enter Your Email : ") #g@g.in , faysalahmadshawun@gmail.com
if len(userEmail)>=6:
    if userEmail[0].isalpha(): #first letter only for alphabet
        if ("@"in userEmail) and (userEmail.count()==1):
            pass
        else:
            print(" Give @ once time ")
    else:
        print(" Invalid Email ")
else:
    print(" Wrong Email")
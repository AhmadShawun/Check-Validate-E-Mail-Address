userEmail = input(" Enter Your Email : ") #g@g.in , faysalahmadshawun@gmail.com
k = 0
if len(userEmail)>=6:
    if userEmail[0].isalpha(): #first letter only for alphabet
        if ("@"in userEmail) and (userEmail.count()==1):
            if (userEmail[-4]==".") ^ (userEmail[-3]=="."):
                for i in userEmail:
                    if i==i.isspace():
                        k = 1
                if k==1:
                    print("Don't use space")
            else:
                print("Must use . ")
        else:
            print(" Give @ once time ")
    else:
        print(" Invalid Email ")
else:
    print(" Wrong Email")
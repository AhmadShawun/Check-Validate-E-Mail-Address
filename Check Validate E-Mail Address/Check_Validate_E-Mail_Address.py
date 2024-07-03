userEmail = input(" Enter Your Email : ") #g@g.in , faysalahmadshawun@gmail.com
k,j,d = 0,0,0
if len(userEmail)>=6:
    if userEmail[0].isalpha(): #first letter only for alphabet
        if ("@"in userEmail) and (userEmail.count("@")==1):
            if (userEmail[-4]==".") ^ (userEmail[-3]=="."):
                for i in userEmail:
                    if i==i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i==i.upper(): # f--F==f
                           j=1 
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("this is not like email address")
            else:
                print("Must use . and write after something")
        else:
            print(" Give @ once time ")
    else:
        print(" Invalid Email ")
else:
    print(" Wrong Email")
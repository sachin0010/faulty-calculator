opt=input("Enetr operator {+ , - , * , / , }: ")
f_no=int(input("Enetr First Number: "))
s_no=int(input("Enter Second Number: "))

if opt=='+':
    if (f_no==55 and s_no==9) or (f_no==9 and s_no==55):
        print("Your ans is 40")
    else:
        print("Your ans is ", f_no+s_no)
elif opt=="-":
    if (f_no==25 and s_no==10) or (f_no==10 and s_no==25):
        print("Your ans is 30")
    else:
        print("Your ans is ",f_no-s_no)
elif opt=="*":
    if (f_no==8 and s_no==5) or (f_no==5 and s_no==8):
        print("Your ans is 21")
    else:
        print("Your ans is ",f_no*s_no)
elif opt=="/":
    if (f_no==80 and s_no==4) or (f_no==4 and s_no==80):
        print("Your ans is 12")
    else:
        print("Your ans is ",f_no/s_no)




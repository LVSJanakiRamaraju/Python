A=input()
B=int(input())
if A=="Monday":
    A=1
elif A=="Tuesday":
    A=2
elif A=="Wednesday":
    A=3
elif A=="Thursday":
    A=4
elif A=="Friday":
    A=5
elif A=="Saturday":
    A=6
else:
    A=0
C=(B+A-1)%7
if C==1:
    print("Monday")
elif C==2:
    print("Tuesday")
elif C==3:
    print("Wednesday")
elif C==4:
    print("Thursday")
elif C==5:
    print("Friday")
elif C==6:
    print("Saturday")
else:
    print("Sunday")
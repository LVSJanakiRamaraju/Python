M=input()
P=input()
M=int(M)
P=int(P)
if (M>35 and P>35) or (M+P>=100):
    print("Qualified")
else:
    print("Not Qualified")
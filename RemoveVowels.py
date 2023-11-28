S=input()
for i in S:
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
        S=S.replace(i,"")
print(S)
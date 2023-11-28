S=input()
f=1
for i in S:
    if i!=i.upper():
        f=0
        break
if f:
    print("True")
else:
    print("False")
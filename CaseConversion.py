S=input()
S=S[:1].lower() + S[1:]
A=""
for i in S:
    if i==i.upper():
        A+="_" + i.lower()
    else:
        A+=i
print(A)
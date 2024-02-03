S = input().split()
A = S[0]
Z = S[0]

for i in S:
    B = i
    if A.lower() > B.lower():
        A = i
    if Z.lower() < B.lower():
        Z = i
print(A + " " + Z)
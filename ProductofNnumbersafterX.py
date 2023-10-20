X=int(input())
N=int(input())
A=1
P=1
while A<=N:
    P*=(X+A)
    A+=1
print(P)
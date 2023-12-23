N=int(input())
K=int(input())
for i in range(N,0,-1):
    if N%i==0:
        K-=1
    if K==0:
        break
if K==0:
    print(i)
else:
    print("1")
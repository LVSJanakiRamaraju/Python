X=input()
N=int(input())
sum=0
A=""
for i in range(1,N+1):
    A=X*i
    A=int(A)**2
    sum+=A
print(sum)
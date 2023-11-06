X=int(input())
N=int(input())
sum=0
for i in range(1,N+1):
    if i%2:
        sum+=X**(2*i)
    else:
        sum-=X**(2*i)
print(sum)
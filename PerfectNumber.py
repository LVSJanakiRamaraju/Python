N=int(input())
sum=0
for i in range(1,(N//2)+1):
    if N%i==0:
        sum+=i
if sum==N:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
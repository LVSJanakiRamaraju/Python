N=input()
len_N=len(N)
sum=0
for i in N:
    sum+=int(i)**len_N
if sum==int(N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
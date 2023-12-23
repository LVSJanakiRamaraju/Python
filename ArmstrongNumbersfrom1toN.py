N=int(input())
for i in range(1,N+1):
    A=str(i)
    len_A=len(A)
    sum=0
    for j in range(0,len_A):
        sum+=int(A[j])**len_A
    if sum==int(A):
        print(A)
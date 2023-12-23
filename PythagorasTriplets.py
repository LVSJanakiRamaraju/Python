N=int(input())
count=0
for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if (i**2 + j**2)==k**2:
                count+=1
print(count)
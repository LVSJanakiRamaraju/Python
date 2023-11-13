N=int(input())
print(" "*(N-1) + "*")
for i in range(2,N+1):
    sp=" "*(N-i)
    print(sp + "*" + " "*(2*(i-1)-1) + "*")
for i in range(N-1,1,-1):
    sp=" "*(N-i)
    print(sp + "*" + " "*(2*(i-1)-1) + "*")
if N>1:
    print(" "*(N-1) + "*")
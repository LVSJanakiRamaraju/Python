N=int(input())
for i in range(1,N+1):
    sp=" "*(2*(N-i) )
    if i==1:
        sp=" "*(2*(N-i) )
        print(sp + "1")
    else:
        print(sp + str(i) + " "*(2*(i-1)-1) + str(i))
for i in range(N-1,0,-1):
    sp=" "*(2*(N-i) )
    if i==1:
        sp=" "*(2*(N-i) )
        print(sp + "1")
    else:
        print(sp + str(i) + " "*(2*(i-1)-1) + str(i))
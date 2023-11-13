N=int(input())
for i in range(1,N+1):
    if i==1 :
        print("* " + "  "*(2*(N-1)) + "*")
    else:
        print("* " + "  "*(i-2) + "* " + "  "*(2*(N-i)) + "* " + "  "*((i-2)) + "*")
for i in range(N,0,-1):
    if i==1 :
        print("* " + "  "*(2*(N-1)) + "*")
    else:
        print("* " + "  "*(i-2) + "* " + "  "*(2*(N-i)) + "* " + "  "*((i-2)) + "*")
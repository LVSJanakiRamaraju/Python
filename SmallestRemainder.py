A=int(input())
B=int(input())
A_B=A%B
B_A=B%A
if A_B<B_A:
    print(A_B)
else:
    print(B_A)
A=input()
B=input()
C=input()
A=int(A)
B=int(B)
C=int(C)
is_A=(A>9) and (A<21)
is_B=(B>9) and (B<21)
is_C=(C>9) and (C<21)
if is_A or is_B or is_C:
    print("True")
else:
    print("False")
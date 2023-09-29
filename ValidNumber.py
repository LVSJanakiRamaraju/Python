N=input()
is_digits=(N[0]!='5') or (N[1]!='5') or (N[2]!='5')
N=int(N)
is_N=(N<700) and (N>300)
if is_digits and is_N:
    print("Valid Number")
else:
    print("Not a Valid Number")
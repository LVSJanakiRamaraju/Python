A=int(input())
Notes_100=int(A/100)
A=A%100
Notes_50=int(A/50)
A=A%50
Notes_20=int(A/20)
A=A%20
Notes_10=int(A/10)
print("100 Notes:",Notes_100)
print("50 Notes:",Notes_50)
print("20 Notes:",Notes_20)
print("10 Notes:",Notes_10)
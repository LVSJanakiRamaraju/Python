A=int(input())
B=int(input())
C=int(input())
if A==B and A==C:
    print("Equilateral Triangle")
elif A==B or A==C or B==C:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
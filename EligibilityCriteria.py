M=input()
P=input()
C=input()
M=int(M)
P=int(P)
C=int(C)
Condition_1=(M>=35) and (P>=35) and (C>=35)
Condition_2=(M+P >= 90) or (P+C >= 90) or (M+C >= 90)
print(Condition_1 and Condition_2)
S=input()
N=int(input())
len_S=len(S)
S_first=S[:N]
S_last=S[len_S-N:]
print(S_first!=S_last)
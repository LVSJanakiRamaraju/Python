A=input()
B=input()
is_coupon=(A[:3]=="DIS") or (B[:3]=="DIS")
if is_coupon:
    print("Discount")
else:
    print("No Discount")
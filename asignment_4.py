def computepay(h,r):
    nrpay=h*r
    expay=(h-40)*(r*0.5)
    pay=nrpay+expay
    return pay

hrs = input("Enter Hours:")
rate= input("enter rates:")
h=float(hrs)
r=float(rate)
if h<=40:
    pay=h*r
    print(pay)
else:
	p = computepay(h,r)
print("Pay",p)
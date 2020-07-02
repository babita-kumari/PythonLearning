hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if h==40:
    pay=h*r
    print(pay)
h=int(h)
if h>=40:
    for (h) in range(40,h+1):
        r+=r*1.5
        pay=h*r
    print(pay)





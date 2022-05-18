# Functions

def computepay(h, r):
    if(h<=40):
        s=(h*r)
    else:
        s=(40*r)+((h-40)*(1.5*r))
    return s

hrs = input("Enter Hours:")
hrs=float(hrs)
rate=input("enter rate")
rate=float(rate)
p = computepay(hrs, rate)
print("Pay", p)

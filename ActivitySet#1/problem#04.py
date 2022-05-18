# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if(h<=40):
     pay=(h*r)
else:
     pay=(h*(r*1.5))
print("pay ",pay)
  

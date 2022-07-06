

def add(a, b):
  c=a+b
  return(c)


def main():
    a = input("Enter 1st Number?")
    a=int(a)
    b = input("Enter 2nd Number?")
    b=int(b)
    c = add(a, b)
    print("Sum of",a," and ",b," is",c)
    

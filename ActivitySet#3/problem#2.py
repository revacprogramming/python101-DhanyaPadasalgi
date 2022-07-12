class fraction:
    def __init__(self,numerator,denominator):
        self.nu=numerator
        self.de=denominator



def number():
    n=input("enter number of egypitan fractions")
    n=int(n)
    return(n)

def entry(n):
    c=list()
    for i in range(n):
        x=int(input("Enter denominator of fraction "))
        element=fraction(1,x)
        print(element)
        c.append(element)
    return(c)

def sum(c,n):
    fn=1
    fd=0
    for i in range(n):
        x=c[i]
        fn=fn*(x.de)
        fd=fd+(x.de)
    ff=fraction(fn,fd)
    return(ff)
    

def main():
    length=number()
    entries=entry(length)
    totalfrac=sum(entries,length)
    print(totalfrac)

# def sumfraction():

if __name__ =='__main__':
    main()

import math
class fraction:
    def __init__(self,numerator,denominator):
        self.nu=int(numerator)
        self.de=int(denominator)



def number():
    n=input("enter number of egypitan fractions")
    n=int(n)
    return(n)

def entry(n):
    c=list()
    for i in range(n):
        x=int(input("Enter denominator of fraction "))
        # print(x)
        element=fraction(1,x)
        # print(element)
        c.append(element)
    return(c)

def sum(c,n):
    fn=0
    fd=1
    for i in range(n):
        x=c[i]
        fn=(fn*x.de)+(1*fd)
        fd=fd*(x.de)
        # print(fn)
        # print(fd)
    ff=fraction(fn,fd)
    return(ff)
    


def reduction(x):
    gcd=math.gcd(x.nu,x.de)
    #print(gcd)
    n=(x.nu)/gcd
    d=(x.de)/gcd
    rf=fraction(n,d)
    return(rf)
# def main():

    # totalfrac=sum(entries,length)
    # print(totalfrac)
    # main()

# def sumfraction():

if __name__ =='__main__':
    length=number()
    entries=entry(length)
    # print(entries)
    ff=sum(entries,length)
    reducedfraction=reduction(ff)
    print(reducedfraction.nu,"/",reducedfraction.de)

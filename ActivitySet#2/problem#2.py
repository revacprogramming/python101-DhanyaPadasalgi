
def add(a, b):
    sum=a+b
    return sum
    pass


def output(a, b, sum):
    print(a,"+",b,"=",sum)
    pass


def main():
    a =input("input?")
    b=input()
    a=int(a)
    b=int(b)
    sum = add(a, b)
    output(a, b, sum)
    

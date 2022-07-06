

def get_cs():
    a=input("enter string")
    return a


def cs_to_lot(cs):
    #print(c)
    cs=cs.split(";")
    # #print(c) 
    x=len(cs)
    #print(x)
    for i in range(x):
        #print(c[i])
        cs[i]=tuple(cs[i].split("="))
        #print(c[i])
    return(cs)

   

def lot_to_cs(l):
    length=len(l)
    for i in range(length):
        l[i]="=".join(l[i])
    l=";".join(l)
    return(l)
    


def main():
    c=get_cs()
    lot=cs_to_lot(c)  # convert connect string to list of tuples
    print(lot)
    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()

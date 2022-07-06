

def get():
    a=input("enter string")
    return a
    


def cs_to_lot(c):
    #print(c)
    c=c.split(";")
    # #print(c) 
    x=len(c)
    #print(x)
    for i in range(x):
        #print(c[i])
        c[i]=tuple(c[i].split("="))
        #print(c[i])
    return(c)



def main():
    cs = get()
    lot = cs_to_lot(cs)
    print(lot)

if __name__ == '__main__':
    main()

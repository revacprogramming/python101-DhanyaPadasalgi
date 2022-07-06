

def get_cs():
    a=input("enter string")
    return a

def cs_to_dict(c):
    d=c.split(";")
    print(c)
    print(d)
    di=dict()
    for i in range(len(d)):
        x=d[i].split("=")
        di[(x[0])]=(x[1])
    return(di)

def dict_to_cs(d):
    l = [(k,"=",v,)
        for k, v in d.items()
    ]
    st = ""
    for i in l:
        a = "".join(i)
        st += f"{a};"
    return st

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()


import math
class coordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y


def output(c,a):
    print("area of ",c.split(",")," is ",a)

def main():
    n=(int(input("enter number of rectangles")))
    j=0
    for j in range(n):
            coord=list()
            l=list()
            for i in range(3):
                x=float(input("enter x coorrdinate"))
                y=float(input("enter y coordinate"))
                coord.append(coordinate(x,y))
        
            print(coord[1].y)
            l=length(coord)
            print(l)
    
    coord=list()
    l=list()

    # for i in range(3):
    #     x=float(input("enter x coorrdinate"))
    #     y=float(input("enter y coordinate"))
    #     coord.append(coordinate(x,y))
    #     # print(coord[i].x)
    # print(coord[1].y)
    # l=length(coord)
    # print(l)
    # ar=area(lengths)
    # print(ar)
    # output(d,a)

def area(A,B,C):
    # A=l[0]
    # B=l[1]
    # C=l[2]
    a=0
    if((math.pow(A,2))>=((math.pow(B,2))+(math.pow(C,2)))):
        a=float((B*C))
        print(B,C)
    elif((math.pow(B,2))>=((math.pow(A,2))+(math.pow(C,2)))):
        a=float((A*C))
        print(A,C)
    else:
        a=float((A*B))
        print(A,B)
    return(a)


def length(c):
    x1=c[0].x
    x2=c[1].x
    x3=c[2].x
    y1=c[0].y
    y2=c[1].y
    y3=c[2].y
    # print(x1,y1,x2,y2,x3,y3)
    a=float((math.sqrt((math.pow((x1-x2),2))+(math.pow((y1-y2),2)))))
    b=float((math.sqrt((math.pow((x2-x3),2))+(math.pow((y2-y3),2)))))
    c=float((math.sqrt((math.pow((x3-x1),2))+(math.pow((y3-y1),2)))))
    # print(a,b,c)
    ar=area(a,b,c)
    return(ar)

    # po=(math.pow(x,2))+(math.pow(y,2))
    # print(po)
    # sq=math.sqrt(po)
    # print(sq)
    # return(sq)


# def working():

    
if __name__ == '__main__':
    main()



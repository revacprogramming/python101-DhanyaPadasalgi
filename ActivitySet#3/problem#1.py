
def area(c):
    x1=c[0].x
    x2=c[1].x
    x3=c[2].x
    y1=c[0].y
    y2=c[1].y
    y3=c[2].y

    area=abs((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2)))
    return(area)


class coordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def main():
    d=list()
    for i in range(3):
        x=input("enter x coorrdinate")
        y=input("enter y coordinate")
        d[i]=coordinate(x,y)
    a=area(d)
    
if __name__ == '__main__':
    main()

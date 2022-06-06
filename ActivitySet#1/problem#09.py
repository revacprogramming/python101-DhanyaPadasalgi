# Lists

#filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip
    x=line.split()
    
    for n in range (len(x)):
        if x[n] not in lst:
            lst.append(x[n])
     
lst.sort()
# print(lst.sort())
print(lst)
            
            
     

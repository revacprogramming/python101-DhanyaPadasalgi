# Loops & Iterators
a=[]
try:
     while True:
        num = input("Enter a number: ")
        num=int(num)
        a.insert(len(a),num)
        print(num)
    
except:
    if num=="done":
        largest=max(a)
        smallest=min(a)
        
        print("Maximum", largest)
        print("minimum", smallest)
    else:
        print("Invaid input")

# Loops & Iterators

largest = None
smallest = None
try:
 while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    elif largest is None or smallest is None:
        num=int(num)
        if num>largest:
            largest=num
            break
        elif num<smallest:
            smallest=num
            break
    print(num)

 print("Maximum", largest)

except:
    print("Invaid input")

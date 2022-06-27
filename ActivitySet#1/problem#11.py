# Tuples

fname = input("Enter file name: ")
fname = fname.strip()
fh = open(fname,'r')
counts=dict()
for line in fh:
    #print(line)
    if line.startswith("From"):
        words=(line.split())
        #print(words)
        time=words[5]
        y=time.split(":")
        print(y)
        word=y[0]
        #print(word)
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
        print(counts)


counts=counts.sort()
print(counts)

            
       

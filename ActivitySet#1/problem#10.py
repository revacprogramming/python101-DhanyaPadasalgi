# Dictionaries

filename = "dataset/mbox-short.txt"
# Dictionaries

name = "mbox-short.txt"

# name = input("Enter file name: ")
name = name.strip()
fh = open(name)
counts=dict()
s=0
maxval=0
for line in fh:
    if line.startswith("From "):
        words=line.split()
    
        # word=words[1:2]
        word = words[1]
        # print(word)
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    if counts[word]>=maxval:
        highest=word
            
print(word, counts[word])
            
#num=list(count.values())
#maxval=num.max()



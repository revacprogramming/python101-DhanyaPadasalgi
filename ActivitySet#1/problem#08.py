# Files
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fname = fname.strip()
fh = open(fname)
count=0
s=0
for line in fh:
 if line.startswith("X-DSPAM-Confidence:"):
  x=line.find("0.")
  numb=line[x:x+6]
  numb=float(numb)
  count=count+1
  s=s+numb
a=s/count
print("Average spam confidence:",a)


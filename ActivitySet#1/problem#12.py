# Regular Expressions
# https://www.py4e.com/lessons/regex
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1546947.txt
fname=input("enter file name")
fname=fname.strip()
sum=0
import re
fh=open(assingment.txt)
for line in fh:
      line=line.strip()
      x=re.findall('([0-9]*)',line)
      x=int(x)
      #print(x)
      sum +=x
print(sum)

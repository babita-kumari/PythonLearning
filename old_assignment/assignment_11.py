#step 1: read through and parse a file with text and numbers.
#step 2: extract all the numbers in the file
# step 3: convert the string into int
# step 4: compute the sum of the numbers

import re
file_name=input("enter file name:")
global_line=open(file_name)
number_list=list()
sum=0
count=0
for line in global_line:
    line=line.rstrip()
    number=re.findall('[0-9]+', line)
    #print(number)
    if len(number)>=0:
        for num in number:
            num=int(num)
            print(num)
            count=count+1
            number_list.append(num)
#print(number_list)
for i in number_list:
    sum+=i
print(sum,count)


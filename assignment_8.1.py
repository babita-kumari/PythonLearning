"""
step1: open file and read line byline
step2: split the line which starts with from
step3:print out second word in the line
step4: print total count of the item in the list at the end
"""

file_name=input("enter file name:")
global_file=open(file_name)
count=0
global_word_list=list()
for line in global_file:
    #line=line.rstrip()
    if line.startswith("From "):
        #print(line)
        words=line.split()
        email_id = words[1]
        global_word_list.append(email_id)
        count += 1

for word in global_word_list:
    print(word)
print("There were", count, "lines in the file with From as the first word")




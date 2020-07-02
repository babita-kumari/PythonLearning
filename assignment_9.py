email_dict=dict()
file_name=input("enter file name:")
global_file=open(file_name)
global_word_list=list()
for line in global_file:
    if line.startswith ("From "):
        words = line.split()
        email_id = words[1]
        global_word_list.append(email_id)
#for word in global_word_list:
    #print(word)
for word in global_word_list:
    email_dict[word]=email_dict.get(word,0)+1
#print(email_dict)
maxcount=None
max_email=None
for email,count in email_dict.items():
    if maxcount is None or count > maxcount:
        max_email=email
        maxcount=count
print(max_email,maxcount)



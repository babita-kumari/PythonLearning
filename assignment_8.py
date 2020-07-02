fname = input("Enter file name: ")
fh = open(fname)
global_word_list = list()

"""
    Step-0: Define global words_list
    Step-1: Read file line by line 
    Step-2: Split each line into words
    Step-3: Append into global_word_list if words in word is not duplicate
    Step-4: Sort global_word_list
    Step-5: Print global word list
"""
for line in fh:
    print(line.rstrip())
    words=line.split()
    #lst.append(word)
    #if word not in lst:continue
    #lst=lst.sort()
    #else:
        #lst.append(word)
    #for word in lst:
    for word in words:
        if word in global_word_list:continue
        else:
            global_word_list.append(word)
global_word_list.sort()
print(global_word_list)
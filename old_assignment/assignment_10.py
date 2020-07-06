time_dict = dict()
global_word_list = list()

file_name = input("enter file name:")
global_file = open(file_name)

for line in global_file:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")
        #print(hour)
        h = hour[0]
        #print(h)
        time_dict[h] = time_dict.get(h, 0) + 1
        x=sorted(time_dict.items())
#print(x[:])
for k,v in x:
    print(k,v)









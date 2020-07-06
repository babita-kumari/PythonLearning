sentence = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
print(sentence)
substring = "car"

count = sentence.count(substring)
print("count is:", count)

count=sentence.count(sentence)
print(count)
words= sentence.split(" ")
print(words)
print(len(words))
counts= dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
bigcount=0
bigword=0
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
print ('Hello world!')






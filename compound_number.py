compound_number = []
for i in range(1,100):
    for j in range(2,i):
        if (i % j)==0:
            compound_number.append(i)
            break
print(compound_number)




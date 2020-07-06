largest = None
smallest =None
numbers= []
while True:
    try:
        num =input("Enter a number: ")
        if num == "done":
            break
        numbers.append(int(num))
    except:
        print("Invalid input")
        False
print(numbers)

for i in numbers:
    if largest is None:
        largest= i
    elif i>largest:
        largest=i
    if smallest is None:
        smallest=i
    elif i<smallest:
        smallest=i
print("Maximum is ", largest)
print("Minumum is", smallest)




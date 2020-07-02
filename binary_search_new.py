list_words=['deepa','pooja','gabbu','anshu','rashmi','putul','maa','amma','pappaji','pappa','shaurya','bannu','tannu']
x='gabbu'
list_words.sort()
print(list_words)
def binary_search(list_words, x):
    low = 0
    high = len(list_words) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if list_words[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif list_words[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

            # If we reach here, then the element was not present
    return -1


# Function call
result = binary_search(list_words, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list_words")
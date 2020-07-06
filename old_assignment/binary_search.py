list_words=['deepa','pooja','gabbu','anshu','rashmi','putul','maa','amma','pappaji','pappa','shaurya','bannu','tannu']
#print(list_words)
list_words.sort()
print(list_words)
x='gabbu'


def binary_search(list_words, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if list_words[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif list_words[mid] > x:
            return binary_search(list_words, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(list_words, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1
result = binary_search(list_words, 0, len(list_words) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list_words")
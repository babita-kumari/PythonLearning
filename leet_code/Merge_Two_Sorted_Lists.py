"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Constructor to initialize the node object
class Solution:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Method to print linked list
    def printList(self):
        temp = self.head

        while temp:
            print(temp.val, end="->")
            temp = temp.next

    # Function to add of node at the end.
    def append(self, new_data):
        new_node = ListNode(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    # Function to merge two sorted linked list.


def mergeTwoLists(l1, l2):
    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if l1 is None:
        return l2

        # if List2 is empty then return List1
    if l2 is None:
        return l1

        # If List1's data is smaller or
    # equal to List2's data
    if l1.val <= l2.val:

        # assign temp to List1's data
        temp = l1

        # Again check List1's data is smaller or equal List2's
        # data and call mergeLists function.
        temp.next = mergeTwoLists(l1.next, l2)

    else:
        # If List2's data is greater than or equal List1's
        # data assign temp to head2
        temp = l2

        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeTwoLists(l1, l2.next)

        # return the temp list.
    return temp


# Driver Function
if __name__ == '__main__':
    # Create linked list :
    # 10->20->30->40->50
    list1 = Solution()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = Solution()
    list2.append(5)
    list2.append(15)
    list2.append(18)
    list2.append(35)
    list2.append(60)

    # Create linked list 3
    list3 = Solution()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = mergeTwoLists(list1.head, list2.head)

    print(" Merged Linked List is : ", end="")
    list3.printList()

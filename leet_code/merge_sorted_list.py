"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""


class Solution:

    def MergeSortedLists(self):
        j = 0
        k = 0
        l1 = [1, 3, 5, 7, 8, 9]
        l2 = [4, 5, 6, 7, 8,10]
        n1 = len(l1)
        n2 = len(l2)
        merge_list = []
        while j <n1 and k <n2:
            print("l1:", l1[j],"l2 :", l2[k])
            if l1[j] <= l2[k]:
                merge_list.append(l1[j])
                j=j+1
            else:
                merge_list.append(l2[k])
                k=k+1
        merge_list=merge_list+l1[j:]+l2[k:]
        return merge_list


object = Solution()
print(object.MergeSortedLists())
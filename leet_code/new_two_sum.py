class Solution:
    def twoSum(self, nums,target):
        solution = {}
        for index, i in enumerate(nums):
            j = target - i

            if j in solution:
                print (solution[j], index)

            else:
                solution[i] = index
        return []


indices = Solution()
indices.twoSum([2,7,11,5], 9)
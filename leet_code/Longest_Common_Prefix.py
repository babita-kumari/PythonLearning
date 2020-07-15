"""
Write a function to find the longest common prefix string amongst an array of strings.

"""



class Solution:
    def longestCommonPrefix(self, strs):
        prefix=""
        strs = sorted(strs)
        n=len(strs)
        g=0
        k=1
        for word in range(1,n):
            result="";
            n1=len(strs[g])
            n2=len(strs[k])
            i=0
            j=0
        while i<=n1-1 and j<=n2-1:
            if strs[g][i]!=strs[k][j]:
                break
            else:
                result=result+strs[g][i]
                i=i+1
                j=j+1
        prefix=result
        g+=1
        k+=1

        return prefix
object = Solution()
print(object.longestCommonPrefix(["flower","flow","flight"]))

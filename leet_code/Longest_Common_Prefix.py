"""
Write a function to find the longest common prefix string amongst an array of strings.

"""



class Solution:
    def longestCommonPrefix(self,strs):
        prefix="";
        a=0
        for word in strs:
            n1=len(word)
            n2=len(strs[a])
            i=0
            j=0
            result = "";
            while i<=n1-1 and j<=n2-1:
                if word[i]!=strs[a][j]:
                    break
                else:
                    result=result+strs[0][i]
                    i=i+1
                    j=j+1
            prefix=result
        a=a+1

        return prefix

object = Solution()
print(object.longestCommonPrefix(["flower","flow","flight"]))

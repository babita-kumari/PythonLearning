class Solution:
    def reverse(self, x):
        reverse_number = 0
        if x>=2**31-1 or x<=-2**31:return 0
        else:
            strx=str(x)
        if strx[0]=='-':
            new_strx=strx[1:]
            reverse_str=new_strx[::-1]
            new_reverse_str='-'+reverse_str
            reverse_number=int(new_reverse_str)
        else:
            reverse_str=strx[::-1]
            reverse_number=int(reverse_str)
        if reverse_number >= 2 ** 31 - 1 or reverse_number <= -2 ** 31:
            return 0
        else:
            return reverse_number

reverse_object = Solution()
print(reverse_object.reverse(1534236469))


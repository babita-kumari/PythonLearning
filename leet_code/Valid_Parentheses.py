"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
solution:
step 1: Declare a character stack S.
step 2: Now traverse the expression string exp.
step 3:If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
step 4: If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if
the popped character is the matching starting bracket then fine else parenthesis are not balanced.
step 5: After complete traversal, if there is some starting bracket left in stack then “not balanced”

"""


class Solution:
    def isValid(self, s: str):
        if len(s)==0:
            return True
        if len(s)==1:
            return False
        if s[0]== ')' or s[0]== '}' or s[0]== ']':
            return False
        string_list = []
        string_dict={}
        string_dict['['] = 0
        string_dict[']'] = 0
        string_dict['{'] = 1
        string_dict['}'] = 1
        string_dict['('] = 2
        string_dict[')'] = 2
        for i in s:
            poped_item = ''
            if i == '(' or i == '{' or i == '[':
                string_list.append(i)
            if i == ')' or i == '}' or i == ']':
                if len(string_list)==0:
                    return False
                i_value=string_dict.get(i)
                last_string=string_list[-1]
                last_string_value=string_dict.get(last_string)
                if i_value == last_string_value:
                    string_list.pop()
                else:
                    return False
        if len(string_list) == 0:
            return True
        else:
            return False


object = Solution()
print(object.isValid("[][{abc}]"))

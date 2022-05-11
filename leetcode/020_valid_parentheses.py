'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        valid = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []

        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            
            else:
                if stack and s[i] == valid.get(stack[-1]):
                    stack.pop()
                else:
                    return False

        return not stack
        
# Run and Test
s = Solution()
print (s.isValid("()[]{]"))
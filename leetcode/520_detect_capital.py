"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_letter_upper = word[0].isupper()
        has_upper = False
        has_lower = False
        for i in range(1, len(word)):
            if word[i].isupper():
                has_upper = True
            else:
                has_lower = True
            
            if has_lower and has_upper:
                break
        
        return (first_letter_upper and has_upper and not has_lower) \
            or (first_letter_upper and not has_upper and has_lower) \
            or (not first_letter_upper and not has_upper and has_lower) \
            or (not has_upper and not has_lower)

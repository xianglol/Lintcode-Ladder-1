
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 00:12:25 2017
@author: lixia

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

---Notice---

Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
Have you met this question in a real interview? Yes

Example
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

"""

class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if len(s) != 0:
            i = 0
            j = len(s) - 1
            while i < j:    # was coding as i - j != 1 and i != j... 
                if not (s[i].isalpha() or s[i].isalnum()):  # to identify if a char is letter or number
                    i += 1
                elif not (s[j].isalpha() or s[j].isalnum()):
                    j -= 1
                elif s[i].upper() == s[j].upper():
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        else:
            return True
#A man, a plan, a canal: Panama

solution = Solution()
print(solution.isPalindrome('1a2'))
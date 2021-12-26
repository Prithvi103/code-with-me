"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
To find a palindrome it's easier to find the center of the palindrome 
and then expand both sides to check the longest palindrome available.
This code runs in O(n^2)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def checkPalindrome(s: str, l: int, i1:int, i2:int):
        while i1>=0 and i2 < len(s):
            if s[i1] == s[i2]:
                l += 2
                i1 -= 1
                i2 += 1
            else:
                break
        return l, i1 + 1, i2
    def longestPalindrome(self, s: str) -> str:
        if s.isspace():
            return ""
        maxlen = 1
        startIndex = 0
        endIndex = 1
        for i in range(len(s)):
            l,st,e = Solution.checkPalindrome(s,0,i-1,i)
            if l > maxlen:
                maxlen = l
                startIndex = st
                endIndex = e
            l,st,e = Solution.checkPalindrome(s,1,i-1,i+1)
            if l > maxlen:
                maxlen = l
                startIndex = st
                endIndex = e
            
        return s[startIndex:endIndex]
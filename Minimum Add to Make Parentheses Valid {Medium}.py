"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or 
')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the 
resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.
"""

"""
One of the fastest times for me to solve a medium level problem on leetcode. Took me just a bit 
over 7 minutes to code the whole thing. The approach is quite simple. I maintained two counters 
for left and right paranthesis and calculated the misbalance everytime a right one was 
encountered. Then I added up the left over unbalanced left paranthesis at the end.
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        result = 0
        left = 0
        right = 0
        if S is None:
            return result
        for i in range(len(S)):
            if S[i] == '(':
                left +=1
            else:
                if left > right:
                    right += 1
                elif right > left:
                    result += 1
                    left += 1
                else:
                    left += 1
                    result += 1
                    right += 1
        result = result + left - right
        return result
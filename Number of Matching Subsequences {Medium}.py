"""
Given string S and a dictionary of words words, find the number of words[i] that is a 
subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

"""
Straightforward solution where I iterate through the string for every word in the words list 
and check if all the characters are available in the same order. I maintain two hash sets of 
words which are subsets of the main string and those which are not to save up on some time. The 
time compleximity of this solution would be O(mn) where m is the length of the string S and n 
is the number of words in the words list
"""


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if S is None or words is None:
            return 0
        count = 0
        for word in words:
            i = 0
            for letter in S:
                if i==len(word):
                    break
                if word[i] == letter:
                    i+=1
            if i == len(word):
                count +=1
                
        return count

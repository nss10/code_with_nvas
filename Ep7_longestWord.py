'''
Leetcode #720. Longest Word in Dictionary (https://leetcode.com/problems/longest-word-in-dictionary/)

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        #convert the list into a set
        
        word_set = set(words)
        maxWord=""
        for word in word_set:
            if len(word) < len(maxWord): 
                continue # stop the processing if the new word is smaller than current maxWord
            
            i=1
            while word[:i] in word_set:
                if i==len(word):
                    maxWord = min(maxWord, word) if i == len(maxWord) else word #verify for lexic order only if lengths are equal
                    break
                i+=1       
        return maxWord
        
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPalindromeString = ""
        maxPalindromeLength = 0
        for idx in range(len(s)):
            # odd case
            currentPalindrome = self.maxPalindrome(s, idx - 1, idx + 1)
            if (len(currentPalindrome) > maxPalindromeLength):
                maxPalindromeString = currentPalindrome
                maxPalindromeLength = len(currentPalindrome)
            # even case
            currentPalindrome = self.maxPalindrome(s, idx, idx + 1)
            if (len(currentPalindrome) > maxPalindromeLength):
                maxPalindromeString = currentPalindrome
                maxPalindromeLength = len(currentPalindrome)
                
        return maxPalindromeString
            
    def maxPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]
            
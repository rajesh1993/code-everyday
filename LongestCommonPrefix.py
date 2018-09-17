'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        prefix = strs[0]
        
        for string in strs:
            idx = 0
            while idx < len(prefix) and idx < len(string) and string[idx] == prefix[idx]:
                idx += 1
            if idx == 0: return ""
            prefix = string[: idx]
        return prefix
                
                    
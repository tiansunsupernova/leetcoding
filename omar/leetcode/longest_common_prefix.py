# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i == len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]
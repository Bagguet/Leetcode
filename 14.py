class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for index in range(len(min(strs, key=len))):
            for i in range(len(strs)-1):
                if strs[i][index]!= strs[i+1][index]:
                    return prefix
            prefix += strs[0][index]

        return prefix

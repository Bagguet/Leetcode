class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        m = len(word1)
        n = len(word2)
        for i in range (max(m, n)):
            if m>i:
                merged += word1[i]
            if n>i:
                merged += word2[i]
        return merged

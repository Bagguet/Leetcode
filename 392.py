class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lastIndex = 0
        t = list(t)
        for i in s:
            isIn = False
            index = lastIndex
            while index<len(t):
                if t[index] == i and lastIndex <= index:
                    isIn = True
                    t[index] = ""
                    lastIndex = index
                    break
                index += 1
            if not isIn:
                return False
        return True

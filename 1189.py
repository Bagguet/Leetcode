class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s = "balloon"
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] =0
            else:
                s_dict[i] =0
        for i in text:
            if i in s_dict:
                s_dict[i] +=1
        s_dict["l"] /=2
        s_dict["o"] /= 2
        return min(s_dict.values())


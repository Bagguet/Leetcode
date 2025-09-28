class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_dict = {}
        result = 0
        for letter in jewels:
            if letter not in jewels_dict:
                jewels_dict[letter] = 0
        for stone in stones:
            if stone in jewels_dict:
                result += 1
        return result


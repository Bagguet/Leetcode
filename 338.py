class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_dict = {}
        for i in ransomNote:
            if i not in ransomNote_dict:
                ransomNote_dict[i] = 1
            else:
                ransomNote_dict[i] += 1
        for i in magazine:
            if i in ransomNote_dict:
                ransomNote_dict[i] -=1
        for item in ransomNote_dict:
            if ransomNote_dict[item] > 0:
                return False
        return True

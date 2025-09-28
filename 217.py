class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 0
            else:
                return True
        return False

        # return True if len(set(nums))< len(nums) else False
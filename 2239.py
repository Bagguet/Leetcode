class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        for num in nums:
            if abs(closest)-abs(num)>0:
                closest = num
            elif abs(closest)-abs(num)==0:
                if closest <num:
                    closest = num
            if closest==0:
                return 0
        return closest
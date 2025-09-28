class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result = [1]*n
        for index in range(1,n):
            result[index] = result[index-1]*nums[index - 1]
        right = 1
        print(result)
        for index in range(n-1,-1,-1):
            result[index] = result[index] * right
            right *= nums[index]
        return result




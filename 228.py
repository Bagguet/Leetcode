class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start = nums[0]
        list_of_numbers = []
        i=1
        on_end =False
        while i<len(nums):
            if nums[i] - nums[i-1] != 1:
                if start == nums[i-1]:
                    list_of_numbers.append(f"{start}")
                else:
                    list_of_numbers.append(f"{start}->{nums[i-1]}")
                start=nums[i]
                if i == len(nums) - 1:
                    on_end = True
            elif start==nums[i]:
                list_of_numbers.append(f"{start}")
                start = nums[i+1]
                if i == len(nums) - 1:
                    on_end = True

            i+=1
        if start==nums[-1]:
            list_of_numbers.append(f"{start}")
        elif not on_end :
            list_of_numbers.append(f"{start}->{nums[i-1]}")
        return list_of_numbers

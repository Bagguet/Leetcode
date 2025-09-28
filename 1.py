from operator import index


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in dict:
                return [dict[new_target], i]
            else:
                dict[nums[i]] = i

def main():
    try:
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
    except ValueError:
        return "Error: Enter int next time ;) "
    if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
        return "NO - That's outside of the map"

    if x1 == x2 or y1 == y2:
        return "YES"
    elif abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"
if __name__ == "__main__":
    print(main())
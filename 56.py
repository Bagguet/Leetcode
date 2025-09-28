class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        results = []
        for interval in intervals:
            if not results or results[-1][1] < interval[0]:
                results.append(interval)
            else:
                results[-1] = [results[-1][0], max(results[-1][1], interval[1])]
        return results
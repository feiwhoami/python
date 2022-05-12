"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key = lambda x : x[0])

        result = [intervals[0]]

        for x in intervals:
            if result[-1][1] >= x[0]:
                result[-1][1] = max(result[-1][1], x[1])
            else:
                result.append(x)

        return result

# Run and Test
s = Solution()
print (s.merge([[1,3],[2,6],[8,10],[15,18]]))
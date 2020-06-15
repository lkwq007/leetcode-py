class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<2:
            return len(intervals)
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ret=[intervals[0]]
        for a,b in intervals[1:]:
            if ret[-1][0]<=a and b<=ret[-1][1]:
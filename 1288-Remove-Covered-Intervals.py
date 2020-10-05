class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<2:
            return len(intervals)
        intervals.sort()
        ret=[intervals[0]]
        for a,b in intervals[1:]:
            if ret[-1][0]<=a and b<=ret[-1][1]:
                continue
            elif a<=ret[-1][0] and ret[-1][1]<=b:
                ret[-1][0]=a
                ret[-1][1]=b
            else:
                ret.append([a,b])
        return len(ret)
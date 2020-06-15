class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        ret=[intervals[0]]
        cur=0
        for a,b in intervals:
            if a<=ret[cur][1]:
                ret[cur][1]=max(b,ret[cur][1])
            else:
                ret.append([a,b])
                cur+=1
        return ret
        
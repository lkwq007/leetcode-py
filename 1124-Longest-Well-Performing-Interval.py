class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # longest positive subarray
        lst=[(1 if item>8 else -1) for item in hours]
        record={}
        record[0]=-1
        acc=0
        ret=0
        for i in range(len(lst)):
            acc+=lst[i]
            last=record.get(acc-1,i)
            if acc>0:
                last=-1
            ret=max(ret,i-last)
            if acc not in record:
                record[acc]=i
        return ret

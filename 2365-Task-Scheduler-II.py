class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        record={}
        cur=0
        for item in tasks:
            last=record.get(item,-space)
            diff=max(0,space-(cur-last))
            cur+=1+diff
            record[item]=cur
        return cur
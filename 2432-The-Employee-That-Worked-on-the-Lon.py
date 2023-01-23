class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        acc=logs[0][1]
        ret=logs[0][0]
        last=acc
        for id, time in logs[1:]:
            cost=time-last
            if cost>acc or (cost==acc and id<ret):
                ret=id
                acc=cost
            last=time
        return ret
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # there is no need to know the headID
        def update(idx):
            if manager[idx]==-1:
                return informTime[idx]
            ret=update(manager[idx])+informTime[idx]
            informTime[idx]=ret
            manager[idx]=-1
            return ret
        max_val=0
        for idx,item in enumerate(informTime,0):
            if item==0:
                ret=update(idx)
                max_val=max(max_val,ret)
        return max_val
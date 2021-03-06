class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1]-x[0],x[1],x[0]))
        ret=0
        for act,req in tasks:
            if ret+act>=req:
                ret+=act
            else:
                ret=req
        return ret
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        last=0
        ret=0
        for i in range(len(rungs)):
            if last+dist<rungs[i]:
                diff=rungs[i]-last
                step=diff//dist
                if diff%dist==0:
                    step-=1
                ret+=step
            last=rungs[i]
        return ret

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        last=0
        ret=0
        for i in range(len(rungs)):
            if last+dist<rungs[i]:
                ret+=(rungs[i]-last-1)//dist
            last=rungs[i]
        return ret
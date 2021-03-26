class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ret=0
        record={}
        for a,b in zip(fronts,backs):
            if a==b:
                record[a]=1
        for a,b in zip(fronts,backs):
            if a not in record:
                if ret==0:
                    ret=a
                else:
                    ret=min(ret,a)
            if b not in record:
                ret=min(ret,b) if ret>0 else b
        return ret
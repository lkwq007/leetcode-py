class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # brute force
        candidates.sort()
        self.ret=[]
        def probe(pos,rest,lst):
            if rest==0:
                self.ret.append(lst[:])
                return
            if pos==len(candidates) or candidates[pos]>rest:
                return
            lst.append(candidates[pos])
            probe(pos,rest-candidates[pos],lst)
            lst.pop()
            probe(pos+1,rest,lst)
        probe(0,target,[])
        return self.ret

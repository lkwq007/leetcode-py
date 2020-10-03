class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ret=[]
        def probe(pos,rest,lst):
            if rest==0:
                self.ret.append(lst[:])
                return
            if pos==len(candidates) or candidates[pos]>rest:
                return
            # use how many?
            next=pos+1
            while next<len(candidates) and candidates[next]==candidates[pos]:
                next+=1
            total=next-pos
            total=min(total,rest//candidates[pos])
            if total<1:
                return
            for i in range(total):
                lst.append(candidates[pos])
                rest-=candidates[pos]
            for i in range(total):
                probe(next,rest,lst)
                rest+=candidates[pos]
                lst.pop()
            probe(next,rest,lst)
        probe(0,target,[])
        return self.ret
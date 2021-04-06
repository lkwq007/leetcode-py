class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.ret=baseCosts[0]
        def probe(idx,acc):
            if idx==len(toppingCosts) or acc>=target:
                if abs(acc-target)<abs(self.ret-target) or abs(acc-target)==abs(self.ret-target) and acc<self.ret:
                    self.ret=acc
                return
            cur=0
            for i in range(3):
                probe(idx+1,acc+cur)
                cur+=toppingCosts[idx]
        for base in baseCosts:
            probe(0,base)
        return self.ret
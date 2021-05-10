class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth={}
        death={}
        for b,d in logs:
            birth[b]=birth.get(b,0)+1
            death[d]=death.get(d,0)+1
        max_val=0
        ret=0
        acc=0
        for i in range(1950,2051):
            acc+=birth.get(i,0)-death.get(i,0)
            if acc>max_val:
                max_val=acc
                ret=i
        return ret
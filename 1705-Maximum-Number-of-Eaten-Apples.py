import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ret=0
        record=[0]*50000
        rest=0
        max_val=0
        for i in range(len(apples)):
            record[i+days[i]]+=apples[i]
            max_val=max(max_val,i+days[i])
            rest+=apples[i]
            rest-=record[i]
            if rest>0:
                ret+=1
                rest-=1
        if rest>
            
            
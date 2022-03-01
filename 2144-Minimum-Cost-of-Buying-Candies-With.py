class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(key=lambda x:-x)
        ret=0
        for i in range(0,len(cost),3):
            ret+=cost[i]
            if i+1<len(cost):
                ret+=cost[i+1]
        return ret
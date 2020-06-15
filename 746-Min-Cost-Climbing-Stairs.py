class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3:
            return min(cost)
        for idx in range(2,len(cost)):
            cost[idx]+=min(cost[idx-1],cost[idx-2])
        return min(cost[-1],cost[-2])
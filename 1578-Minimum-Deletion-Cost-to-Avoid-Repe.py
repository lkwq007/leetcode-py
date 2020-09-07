class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ret=0
        last=""
        acc=0
        max_val=0
        for i in range(len(s)):
            item=s[i]
            if last==item:
                acc+=cost[i]
                max_val=max(max_val,cost[i])
            else:
                ret+=acc-max_val
                acc=cost[i]
                max_val=cost[i]
            last=item
        return ret+acc-max_val
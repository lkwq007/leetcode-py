class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # can greedy work?
        def dfs(x):
            if x>n:
                return 0,0
            left=x*2
            right=x*2+1
            l0,l1=dfs(left)
            r0,r1=dfs(right)
            diff=abs(l0-r0)
            return (cost[x-1]+max(l0,r0),l1+r1+diff)
        return dfs(1)[1]

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # build graph
        graph=[[] for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(1,d+1):
                if i+j<len(arr) and arr[i+j]<arr[i]:
                    graph[i].append(i+j)
                else:
                    break
            for j in range(1,d+1):
                if i-j>=0 and arr[i-j]<arr[i]:
                    graph[i].append(i-j)
                else:
                    break
        dp=[-1]*len(arr)
        def dfs(idx):
            if dp[idx]!=-1:
                return dp[idx]
            ret=1
            for next in graph[idx]:
                ret=max(ret,dfs(next)+1)
            dp[idx]=ret
            return ret
        acc=0
        for i in range(len(arr)):
            acc=max(dfs(i),acc)
        return acc
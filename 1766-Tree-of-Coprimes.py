class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # 1 <= nums[i] <= 50
        # worst case
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        coprime=[[0]*51 for _ in range(51)]
        for i in range(1,51):
            for j in range(i,51):
                if gcd(i,j)==1:
                    coprime[i][j]=1
                    coprime[j][i]=1
        graph=[[] for _ in range(len(nums))]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ret=[-1]*len(nums)
        def dfs(x,acc,par,level,mapping):
            val=nums[x]
            idx=-1
            for i in range(1,51):
                if coprime[i][val]==1 and level[i]!=-1:
                    if idx==-1 or level[idx]<level[i]:
                        idx=i
            if idx!=-1:
                ret[x]=mapping[idx]
            prev0=level[val]
            prev1=mapping[val]
            level[val]=acc
            mapping[val]=x
            for next in graph[x]:
                if next==par:
                    continue
                dfs(next,acc+1,x,level,mapping)
            level[val]=prev0
            mapping[val]=prev1
        dfs(0,0,-1,[-1]*51,[-1]*51)
        return ret
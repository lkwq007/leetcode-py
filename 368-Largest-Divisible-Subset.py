from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        nums.sort()
        dp=[[item] for item in nums]
        ret=0
        for i in range(1,len(nums)):
            max_idx=-1
            for j in range(0,i):
                if nums[i]%nums[j]==0:
                    if max_idx<0 or len(dp[max_idx])<len(dp[j]):
                        max_idx=j
            if max_idx!=-1:
                dp[i]=dp[max_idx][:]
                dp[i].append(nums[i])
            if len(dp[ret])<len(dp[i]):
                ret=i
        return dp[ret]
        

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # connected component?
        # distinct
        if len(nums)<2:
            return nums
        nums.sort(reverse=True)
        graph=[{} for _ in range(len(nums))]
        in_degree=[0]*len(nums)
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]%nums[j]==0:
                    graph[i][j]=1
                    in_degree[j]+=1
                elif nums[j]%nums[i]==0:
                    graph[j][i]=1
                    in_degree[i]+=1
        self.ret=[0]
        def dfs(node,lst):
            lst.append(node)
            if not graph[node]:
                if len(lst)>len(self.ret):
                    self.ret=lst[:]
            else:
                for item in graph[node]:
                    if graph[node][item]:
                        for parent in lst[:-1]:
                            if item in graph[parent]:
                                graph[parent][item]=0
                        dfs(item,lst)
            lst.pop()
        for idx in range(len(in_degree)):
            if in_degree[idx]==0:
                dfs(idx,[])
        return list(map(lambda x:nums[x],self.ret))
x=Solution()
print(x.largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]))
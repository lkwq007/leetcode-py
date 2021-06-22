class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if k==1:
            return sum(arr)
        if k==len(arr):
            return len(arr)*max(arr)
        dp=[0]*(len(arr)+1)
        dp[0]=arr[0]
        for i in range(1,len(arr)):
            acc=0
            j=0
            while j<k and i-j>=0:
                acc=max(acc,arr[i-j])
                dp[i]=max(dp[i],dp[i-j-1]+acc*(j+1))
                j+=1
        return dp[-2]
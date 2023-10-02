class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ret=0
        for i in range(len(maxHeights)):
            left=0
            right=0
            acc=maxHeights[i]
            for j in range(i-1,-1,-1):
                acc=min(acc,maxHeights[j])
                left+=acc
            acc=maxHeights[i]
            for j in range(i+1,len(maxHeights)):
                acc=min(acc,maxHeights[j])
                right+=acc
            ret=max(ret,left+right+maxHeights[i])
        return ret
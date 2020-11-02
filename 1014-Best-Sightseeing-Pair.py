class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ret=0
        # brute force
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                ret=max(A[j]+A[i]+i-j,ret)
        return ret
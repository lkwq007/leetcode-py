class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A)<2:
            return 0
        if K==0:
            return max(A)-min(A)
        A.sort()
        ret=A[-1]-A[0]
        for i in range(len(A)-1):
            lst=[A[0]+K,A[i]+K,A[i+1]-K,A[-1]-K]
            ret=min(ret,max(lst)-min(lst))
        return ret
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        idx=0
        total=len(A)
        while idx<total:
            if (idx+1<total and A[idx]==A[idx+1]) or (idx+2<total and A[idx]==A[idx+2]) or (idx+3<total and A[idx]==A[idx+3]):
                return A[idx]
            idx+=1
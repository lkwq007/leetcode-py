class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc=True
        dec=True
        total=len(A)-1
        idx=0
        while idx<total:
            if A[idx+1]>A[idx]:
                dec=False
            if A[idx+1]<A[idx]:
                inc=False
            if not (inc or dec):
                return False
            idx+=1
        return True
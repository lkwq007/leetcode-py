class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        max_val=0
        n=len(A)
        for k in range(0,n):
            acc=0
            for idx in range(0,n):
                acc+=A[idx]*((idx-k)%n)
            max_val=max(acc,max_val)
        return max_val
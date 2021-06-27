class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n=len(A)
        k=0
        acc=0
        for idx in range(0,n):
            acc+=A[idx]*((idx-k)%n)
        max_val=acc
        total=sum(A)
        for k in range(1,n):
            acc=acc+total-A[n-k]*n
            max_val=max(max_val,acc)
        return max_val
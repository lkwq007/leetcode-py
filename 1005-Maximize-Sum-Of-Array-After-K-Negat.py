class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        idx=0
        while idx<len(A) and idx<K and A[idx]<=0:
            if A[idx]==0:
                return sum(A)
            A[idx]=-A[idx]
            idx+=1
        if idx>=K or (K-idx)%2==0:
            return sum(A)
        total=sum(A)
        if idx>=len(A):
            idx-=1
        prev=A[idx] if idx==0 else A[idx-1]
        cur=A[idx]
        return max(total-2*prev,total-2*cur)
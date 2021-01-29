class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # prefix
        ret=0
        acc=0
        for i in range(len(A)):
            acc+=A[i]
            A[i]=acc
        total=min(len(A),len(A)-L-M+1)
        for i in range(total):
            left=0 if i==0 else A[i-1]
            for j in range(i+L,len(A)-M+1):
                tmp=A[i+L-1]-left+A[j+M-1]-A[j-1]
                ret=max(ret,tmp)
            for j in range(i+M,len(A)-L+1):
                tmp=A[i+M-1]-left+A[j+L-1]-A[j-1]
                ret=max(ret,tmp)
        return ret

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        acc=0
        for i in range(len(A)):
            acc+=A[i]
            A[i]=acc
        ret=A[L+M-1]
        maxL=A[L-1]
        maxM=A[M-1]
        for i in range(L+M,len(A)):
            maxL=max(maxL,A[i-M]-A[i-M-L])
            maxM=max(maxM,A[i-L]-A[i-L-M])
            ret=max(ret,maxL+A[i]-A[i-M],maxM+A[i]-A[i-L])
        return ret
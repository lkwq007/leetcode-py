class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A)<2:
            return 0
        total=len(A[0])
        ret=0
        for i in range(total):
            for j in range(len(A)-1):
                if A[j+1][i]<A[j][i]:
                    ret+=1
                    break
        return ret
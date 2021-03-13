class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        # brute force
        term=10**9+7
        record={}
        A.sort()
        for item in A:
            record[item]=1
        ret=0
        for i in range(len(A)):
            acc=1
            for j in range(i):
                if A[i]%A[j]==0 and A[i]//A[j] in record:
                    left=record[A[j]]
                    right=record[A[i]//A[j]]
                    acc+=left*right
            record[A[i]]=acc
            ret+=acc
            ret%=term
        return ret

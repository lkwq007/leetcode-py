class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # brute force
        ret=1
        lst=[{} for _ in range(len(A))]
        for i in range(len(A)):
            record=lst[i]
            for j in range(i+1,len(A)):
                diff=A[j]-A[i]
                cnt=record.get(diff,0)+1
                lst[j][diff]=max(lst[j].get(diff,0),cnt)
                ret=max(lst[j][diff],ret)
        return ret+1

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # brute force
        record={}
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                record[(j,A[j]-A[i])]=record.get((i,A[j]-A[i]),1)+1
        return max(record.values())
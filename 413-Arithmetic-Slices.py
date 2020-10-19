class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ret=0
        cnt=0
        if len(A)<3:
            return 0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                cnt+=1
                ret+=cnt
            else:
                cnt=0
        return ret
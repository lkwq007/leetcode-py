class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A)<2:
            return 0
        ret=0
        A.sort()
        cur=A[0]-1
        for i in range(len(A)):
            item=A[i]
            if item>cur:
                cur=item
            else:
                cur+=1
                ret+=cur-item
        return ret
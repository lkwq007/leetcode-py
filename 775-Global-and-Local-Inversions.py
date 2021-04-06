class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)-1):
            if A[i]>A[i+1]+1:
                return False
            if i+2<len(A) and A[i]>A[i+1] and A[i+1]>A[i+2]:
                return False
        return True
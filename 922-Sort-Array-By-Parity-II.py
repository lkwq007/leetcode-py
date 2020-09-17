class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i=0
        j=1
        while i<len(A) and j<len(A):
            while i<len(A):
                if A[i]&1:
                    break
                i+=2
            while j<len(A):
                if A[j]&1==0:
                    break
                j+=2
            if i<len(A) and j<len(A):
                A[i],A[j]=A[j],A[i]
        return A
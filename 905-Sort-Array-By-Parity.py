class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i=0
        j=0
        total=len(A)
        while i<total and j<total:
            if A[i]%2==0:
                A[j],A[i]=A[i],A[j]
                i+=1
                j+=1
            else:
                i+=1
        return A
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(key=lambda x:-x)
        for i in range(2,len(A)):
            if A[i]+A[i-1]>A[i-2]:
                return A[i]+A[i-1]+A[i-2]
        return 0

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[]
        for item in matrix:
            lst+=item
        lst.sort()
        return lst[k-1]
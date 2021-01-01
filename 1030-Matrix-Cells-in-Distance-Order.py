class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret=[]
        for i in range(R):
            for j in range(C):
                ret.append([i,j])
        ret.sort(key=lambda x:abs())
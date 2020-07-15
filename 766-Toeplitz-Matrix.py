class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix)<2 or len(matrix[0])<2:
            return  True
        h=len(matrix)
        w=len(matrix[0])
        for y in range(0,h-1):
            cur=matrix[y][0]
            for i in range(1,h):
                if i>=w or y+i>=h:
                    break
                if cur!=matrix[y+i][i]:
                    return False
        for x in range(1,w-1):
            cur=matrix[0][x]
            for i in range(1,h):
                if i>=h or x+i>=w:
                    break
                if cur!=matrix[i][x+i]:
                    return False
        return True
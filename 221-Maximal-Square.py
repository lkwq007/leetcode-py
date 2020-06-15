class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        max_area=0
        h=len(matrix)
        w=len(matrix[0])
        tmp=[0]*(w+1)
        table=[None]*(h+1)
        for i in range(0,h+1):
            table[i]=tmp[:]
        for y in range(1,h+1):
            for x in range(1,w+1):
                if matrix[y-1][x-1]=="1":
                    table[y][x]=min(table[y-1][x],table[y-1][x-1],table[y][x-1])+1
                    max_area=max(max_area,table[y][x])
        return max_area*max_area
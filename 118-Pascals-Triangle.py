class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows<2:
            return [[1]]
        ret=[[1]]
        for i in range(1,numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=ret[-1][j-1]+ret[-1][j]
            ret.append(row)
        return ret
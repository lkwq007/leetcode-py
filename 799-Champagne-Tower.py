class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses=[[0]*100 for _ in range(100)]
        excess=[[0]*100 for _ in range(100)]
        if poured<2:
            glasses[0][0]=poured
            return glasses[query_row][query_glass]
        glasses[0][0]=1.0
        excess[0][0]=poured-1
        eps=1e-20
        for i in range(1,query_row+1):
            total=sum(excess[i-1])
            if total<eps:
                break
            for j in range(i+1):
                if j==0:
                    glasses[i][j]=excess[i-1][j]/2  
                else:
                    glasses[i][j]=excess[i-1][j-1]/2+excess[i-1][j]/2
                if glasses[i][j]>1.0:
                    excess[i][j]=glasses[i][j]-1
                    glasses[i][j]=1
        return glasses[query_row][query_glass]


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # wrong simulation, TLE
        glasses=[[0 for _ in range(100)] for _ in range(100)]
        eps=1e-20
        def pour(row,pos,amount):
            if row>=100:
                return
            if glasses[row][pos]>1.0-eps:
                pour(row+1,pos,amount/2.0)
                pour(row+1,pos+1,amount/2.0)
            elif glasses[row][pos]+amount>1.0-eps:
                excess=glasses[row][pos]+amount-1.0
                pour(row+1,pos,excess/2.0)
                pour(row+1,pos+1,excess/2.0)
            else:
                glasses[row][pos]+=amount
        for i in range(poured):
            pour(0,0,1.0)
        return glasses[query_row][query_glass]

x=Solution()
x.champagneTower(20,0,0)
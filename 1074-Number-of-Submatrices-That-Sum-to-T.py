class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        h=len(matrix)
        w=len(matrix[0])
        template=[0]*(w+1)
        dp=[template[:] for _ in range(h+1)]
        acc=0
        for x in range(w):
            dp[0][x]=matrix[0][x]+acc
            acc=dp[0][x]
        acc=0
        for y in range(h):
            dp[y][0]=matrix[y][0]+acc
            acc=dp[y][0]
        for y in range(1,h):
            for x in range(1,w):
                dp[y][x]=matrix[y][x]+dp[y-1][x]+dp[y][x-1]-dp[y-1][x-1]
        ret=0
        # [print(item) for item in dp]
        
        for x0 in range(w):
            for x1 in range(x0,w):
                record={0:1}
                # record={}
                for y in range(h):
                    # print(x0,x1,y,record)
                    val=dp[y][x1]-dp[y][x0-1]
                    # print(x0,x1,y,val,target-val)
                    diff=val-target
                    ret+=record.get(diff,0)
                    record[val]=record.get(val,0)+1
        return ret
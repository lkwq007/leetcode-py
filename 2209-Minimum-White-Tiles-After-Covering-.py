class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # brute force
        total=sum(map(int,floor))
        dp=[[0]*(numCarpets+1) for _ in range(floor)]
        acc=0
        for i in range(carpetLen):
            if floor[i]=="1":
                acc+=1
        for i in range(carpetLen):
            dp[carpetLen-1][i]=acc
        for i in range(carpetLen,len(floor)):

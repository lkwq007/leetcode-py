class Solution:
    def numTrees(self, n: int) -> int:
        record=[1]*(n+1)
        for i in range(2,n+1):
            acc=0
            for j in range(0,i):
                if j==0 or j==i-1:
                    acc+=record[i-1]
                else:
                    acc+=record[j]*record[i-j-1]
            record[i]=acc
        return record[n]
x=Solution()
print(x.numTrees(1))
print(x.numTrees(2))
print(x.numTrees(3))
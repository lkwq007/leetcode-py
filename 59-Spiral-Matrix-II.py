class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total_offset=(n+1)//2
        template=[0]*n
        ret=[template[:] for _ in range(n)]
        val=1
        for offset in range(total_offset):
            if n-offset*2-1==0:
                ret[offset][offset]=val
            for i in range(n-offset*2-1):
                ret[offset][offset+i]=val
                val+=1
            for i in range(n-offset*2-1):
                ret[offset+i][n-offset-1]=val
                val+=1
            for i in range(n-offset*2-1):
                ret[n-offset-1][n-offset-i-1]=val
                val+=1
            for i in range(n-offset*2-1):
                ret[n-offset-i-1][offset]=val
                val+=1
        return ret
            
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total_offset=(n+1)//2
        template=[0]*n
        ret=[template[:] for _ in range(n)]
        val=1
        for offset in range(total_offset):
            step=n-offset*2-1
            if step==0:
                ret[offset][offset]=val
            for i in range(step):
                ret[offset][offset+i]=val
                ret[offset+i][n-offset-1]=ret[offset][offset+i]+step
                ret[n-offset-1][n-offset-i-1]=ret[offset+i][n-offset-1]+step
                ret[n-offset-i-1][offset]=ret[n-offset-1][n-offset-i-1]+step
                val+=1
            val+=3*step
        return ret
            

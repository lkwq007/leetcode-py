class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        record={}
        dp={}
        for y,x in mines:
            record[(y,x)]=1
        ret=0
        for y in range(N):
            for x in range(N):
                if (y,x) not in record:
                    offset=0
                    while True:
                        offset+=1
                        cnt=0
                        for y0,x0 in [(y-offset,x),(y+offset,x),(y,x-offset),(y,x+offset)]:
                            if (y0,x0) in record or y0<0 or y0>=N or x0<0 or x0>=N:
                                cnt+=1
                            else:
                                dp
                        if cnt>0:
                            break
                    ret=max(offset,ret)
        return ret
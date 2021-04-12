class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k<2:
            return [i+1 for i in range(n)]
        lst=[]
        start=1
        end=n
        record={}
        cnt=0
        while start<=end:
            if cnt+2<=k:
                lst.append(end)
                lst.append(start)
                cnt+=2
                start+=1
                end-=1
            elif cnt+1<=k and start+1==end:
                lst.append(end)
                lst.append(start)
                cnt+=1
                start+=1
                end-=1
            else:
                lst.append(start)
                start+=1
        return lst

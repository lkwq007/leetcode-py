class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minval=256
        maxval=0
        acc=0
        mode=0
        mode_val=count[0]
        cnt=0
        total=sum(count)
        median=0
        if total%2==1:
            idx=[total//2]
        else:
            idx=[(total-1)//2,total//2]
        median=[0]
        def feed(cnt,i):
            if len(idx)==1:
                if cnt<idx[0]+1 and cnt+count[i]>=idx[0]+1:
                    median[0]=i
            else:
                if cnt<idx[0]+1:
                    if cnt+count[i]>idx[0]+1:
                        median[0]=i
                    elif cnt+count[i]==idx[0]+1:
                        for next in range(i+1,len(count)):
                            if count[next]>0:
                                break
                        median[0]=(i+next)/2
        for i in range(len(count)):
            if mode_val<count[i]:
                mode=i
                mode_val=count[i]
            acc+=i*count[i]
            if count[i]>0:
                minval=min(minval,i)
                maxval=i
            feed(cnt,i)
            cnt+=count[i]
        return [minval,maxval,acc/total,median[0],mode]
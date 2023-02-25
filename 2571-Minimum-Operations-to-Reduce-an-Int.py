class Solution:
    def minOperations(self, n: int) -> int:
        # bfs?
        ret=0
        record={n:1}
        queue=[n]
        while queue:
            target=[]
            ret+=1
            for item in queue:
                cur=1
                for i in range(32):
                    if cur>item:
                        break
                    for next in [item-cur,item+cur]:
                        if next==0:
                            return ret
                        if next not in record:
                            record[next]=1
                            target.append(next)
                    cur=cur<<1
            queue=target
        return ret
                    
class Solution:
    def minOperations(self, n: int) -> int:
        ret=0
        cnt=0
        while n>0:
            if n&1:
                cnt+=1
            else:
                if cnt==1:
                    ret+=1
                    cnt=0
                elif cnt>1:
                    cnt=1
                    ret+=1
                else:
                    cnt=0
            n=n>>1
        if cnt>1:
            ret+=2
        elif cnt>0:
            ret+=1
        return ret

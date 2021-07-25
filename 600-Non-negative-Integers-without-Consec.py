class Solution:
    def findIntegers(self, n: int) -> int:
        cnt=0
        num=n
        lst=[]
        while num>0:
            lst.append(num&1)
            cnt+=1
            num=num>>1
        count=[0]*cnt
        count[-1]=1
        even=1
        odd=1
        for i in range(cnt-1):
            count[i]=even+odd
            even,odd=even+odd,even
        ret=0
        lst=lst[::-1]
        flag=True
        for i in range(1,len(lst)):
            if lst[i]==1 and lst[i-1]==1:
                ret+=count[cnt-i-2]
                flag=False
                break
            elif lst[i]==1:
                ret+=count[cnt-i-2]
        if flag:
            ret+=1
        return count[cnt-2]+ret

class Solution:
    def findIntegers(self, n: int) -> int:
        # brute force, TLE 
        queue=[1]
        ret=1
        while queue:
            ret+=len(queue)
            target=[]
            for item in queue:
                next=item<<1
                if next<=n:
                    target.append(next)
                if item&1==0 and (next|1)<=n:
                    target.append(next|1)
            queue=target
        return ret
class Solution:
    def countLargestGroup(self, n: int) -> int:
        record={}
        def count(x):
            ret=0
            while x>0:
                ret+=(x%10)
                x=x//10
            return ret
        cnt=0
        max_val=0
        for i in range(1,n+1):
            if i%10==0:
                cnt=count(i)
            else:
                cnt+=1
            tmp=record.get(cnt,0)+1
            max_val=max(tmp,max_val)
            record[cnt]=tmp
        ret=0
        for key,val in record.items():
            if val==max_val:
                ret+=1
        return ret
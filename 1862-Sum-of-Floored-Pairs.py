class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        count=[0]*200001
        max_val=0
        for item in nums:
            count[item]+=1
            max_val=max(item,max_val)
        ret=0
        term=10**9+7
        prefix=count[:]
        acc=0
        for i in range(len(prefix)):
            prefix[i]+=acc
            acc=prefix[i]
        for i in range(len(count)):
            if count[i]>0:
                cur=i
                cnt=1
                while cur<=max_val:
                    ret+=(prefix[cur+i-1]-prefix[cur-1])*count[i]*cnt
                    cnt+=1
                    cur+=i
                    ret%=term
        return ret



class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        # TLE
        count=[0]*100001
        for item in nums:
            count[item]+=1
        ret=0
        term=10**9+7
        prefix=count[:]
        acc=0
        def process(x):
            cur=1
            cnt=0
            while True:
                tmp=prefix[x//cur]-prefix[x//(cur+1)]
                if prefix[x//cur]<1:
                    break
                cnt+=cur*tmp
                cnt%=term
                cur+=1
            return cnt
        for i in range(len(prefix)):
            prefix[i]+=acc
            acc=prefix[i]
            if count[i]>0:
                ret+=process(i)*count[i]
                ret%=term
        return ret

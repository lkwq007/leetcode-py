class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        plist=[]
        total=max(nums)
        prime=[0]*(total+1)
        for i in range(2,total+1):
            if prime[i]==0:
                prime[i]=i
                plist.append(i)
            j=0
            while j<len(plist) and plist[j]<=prime[i] and i*plist[j]<=total:
                prime[i*plist[j]]=plist[j]
                j+=1
        lst=set(nums)
        precord={item:1 for item in plist}
        ret=0
        acc=0
        for i in range(2,total+1):
            if i in lst:
                ret+=1
                if i in precord:
                    acc+=1
            else:
                cnt=0
                j=2
                while j*i<=total
                    cur=j*i
                    if cur>total:
                        break
                    if cur in lst:
                        cnt+=1
                    if cnt==2:
                        ret+=1
                        if i in precord:
                            acc+=1
                        break                
        return ret+(1 if acc>1 else 0)

import functools
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # TLE
        plist=[]
        total=max(nums)
        prime=[0]*(total+1)
        for i in range(2,total+1):
            if prime[i]==0:
                prime[i]=i
                plist.append(i)
            j=0
            while j<len(plist) and plist[j]<=prime[i] and i*plist[j]<=total:
                prime[i*plist[j]]=plist[j]
                j+=1
        prime_set={item:1 for item in plist}
        prime_set[1]=1
        @functools.lru_cache(maxsize=None)
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        record={}
        precord={}
        nums=list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            item=nums[i]
            target={}
            if item in prime_set:
                precord[item]=1
            else:
                target[item]=1
            for key in record.keys():
                a,b=key,item
                if a<b:
                    a,b=b,a
                cur=gcd(a,b)
                if cur in prime_set:
                    precord[cur]=1
                else:
                    target[cur]=1
            for key in target.keys():
                record[key]=1
        if len(precord)>1:
            precord[1]=1
        return len(record)+len(precord)
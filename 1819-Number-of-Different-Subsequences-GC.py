class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        lst=set(nums)
        total=max(nums)
        ret=0
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        for i in range(1,total+1):
            if i in lst:
                ret+=1
            else:
                j=i
                acc=0
                while j<=total:
                    if j in lst:
                        acc=gcd(j,acc)
                    j+=i
                    if acc==i:
                        break
                if acc==i:
                    ret+=1
        return ret

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # python TLE
        record=[-1]*(max(nums)+1)
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        nums=list(set(nums))
        nums.sort()
        lst=set(nums)
        ret=0
        for item in nums:
            i=1
            while i*i<=item:
                if item%i==0:
                    if record[i]==-1:
                        record[i]=item//i
                    else:
                        record[i]=gcd(record[i],item//i)
                    if record[item//i]==-1:
                        record[item//i]=i
                    else:
                        record[item//i]=gcd(record[item//i],i)
                i+=1
        for i in range(1,max(nums)+1):
            if record[i]==1 or i in lst:
                ret+=1
        return ret

import functools
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # TLE
        @functools.lru_cache(maxsize=None)
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        record={}
        for i in range(len(nums)):
            item=nums[i]
            target={}
            target[item]=1
            for key in record.keys():
                a,b=key,item
                if a<b:
                    a,b=b,a
                target[gcd(a,b)]=1
            for key in target.keys():
                record[key]=1
        return len(record)
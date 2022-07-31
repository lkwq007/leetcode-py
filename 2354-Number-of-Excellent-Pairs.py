class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # a|b + a&b a+b
        def count(x):
            acc=0
            while x>0:
                acc+=(x&1)
                x=x>>1
            return acc
        nums=set(nums)
        nums=sorted([count(item) for item in nums])
        ret=0
        # for item in nums:
        #     if item*2>=k:
        #         ret-=1
        for i in range(len(nums)):
            cur=nums[i]
            rest=k-cur
            left=0
            right=len(nums)
            while left<right:
                middle=left+(right-left)//2
                if nums[middle]<rest:
                    left=middle+1
                else:
                    right=middle
            ret+=len(nums)-left
        return ret

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def count(x):
            acc=0
            while x>0:
                acc+=(x&1)
                x=x>>1
            return acc
        nums=set(nums)
        nums=sorted([count(item) for item in nums])
        ret=0
        left=0
        for i in range(len(nums)-1,-1,-1):
            cur=nums[i]
            rest=k-cur
            while left<len(nums) and nums[left]<rest:
                left+=1
            ret+=len(nums)-left
        return ret

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def count(x):
            acc=0
            while x>0:
                acc+=(x&1)
                x=x>>1
            return acc
        nums=set(nums)
        record=[0]*64
        for item in nums:
            record[count(item)]+=1
        ret=0
        for i in range(len(record)):
            for j in range(len(record)):
                if i+j>=k:
                    ret+=record[i]*record[j]
        return ret


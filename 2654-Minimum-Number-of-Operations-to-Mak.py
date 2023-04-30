class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a,b):
            cnt=0
            while b:
                a,b=b,a%b
                cnt+=1
            return a,cnt
        acc=nums[0]
        min_cnt=10**6
        ones=1 if nums[0]==1 else 0
        for i in range(1,len(nums)):
            val,cnt=gcd(nums[i-1],nums[i])
            min_cnt=min(min_cnt,cnt)
            acc=gcd(acc,val)
            if nums[i]==1:
                ones+=1
        if acc>1:
            return -1
        if ones>0:
            return len(nums)-ones
        return min_cnt+len(nums)-1
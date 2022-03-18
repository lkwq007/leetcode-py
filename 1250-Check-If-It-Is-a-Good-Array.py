class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        acc=nums[0]
        for item in nums:
            acc=gcd(acc,item)
            if acc==1:
                return True
        return False
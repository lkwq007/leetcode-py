class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        numsDivide.sort()
        acc=numsDivide[0]
        for item in numsDivide[1:]:
            acc=gcd(item,acc)
            if acc==1:
                break
        nums.sort()
        for i in range(len(nums)):
            if acc%nums[i]==0:
                return i
        return -1
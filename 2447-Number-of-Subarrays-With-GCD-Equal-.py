class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        ret=0
        for i in range(len(nums)):
            acc=nums[i]
            if acc>=k and acc%k==0:
                for j in range(i,len(nums)):
                    acc=gcd(acc,nums[j])
                    if acc<k or acc%k:
                        break
                    if acc==k:
                        ret+=1
        return ret
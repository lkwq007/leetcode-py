class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total=len(nums)
        # element [0,10^9]
        count=[0]*31
        mask=[1<<i for i in range(31)]
        for item in nums:
            for i in range(31):
                if item&mask[i]:
                    count[i]+=1
        ret=0
        for i in range(31):
            if count[i]>0:
                ones=count[i]
                zeros=total-count[i]
                ret+=ones*zeros
        return ret
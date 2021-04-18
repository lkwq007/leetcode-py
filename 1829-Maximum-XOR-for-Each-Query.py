class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        acc=0
        for item in nums:
            acc^=item
        ret=[]
        def find(x):
            mask=1<<(maximumBit-1)
            ret=0
            while mask>0:
                ret=ret<<1
                if mask&x==0:
                    ret+=1
                mask=mask>>1
            return ret
        for i in range(len(nums)-1,-1,-1):
            val=find(acc)
            ret.append(val)
            acc^=nums[i]
        return ret

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        acc=0
        ret=[0]*len(nums)
        val=(1<<maximumBit)-1
        for i in range(len(nums)):
            acc^=nums[i]
            ret[len(nums)-1-i]=val^acc
        return ret
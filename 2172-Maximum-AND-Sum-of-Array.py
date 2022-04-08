class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # select slots using nums
        mask=1
        mapping=[0]*(2*numSlots)
        for i in range(len(mapping)):
            mapping[i]=mask
            mask=mask<<1
        import functools
        @functools.lru_cache(None)
        def probe(acc,pos):
            if pos>=len(nums):
                return 0
            cur=nums[pos]
            ret=probe(acc,pos+1)
            for i in range(0,len(mapping),2):
                mask=mapping[i]
                mask2=mapping[i+1]
                slot=i//2+1
                val=cur&slot
                if val:
                    if mask&acc==0 and mask2&acc==0:
                        ret=max(ret,val+probe(acc|mask,pos+1))
                    elif mask&acc!=0 and mask2&acc==0:
                        ret=max(ret,val+probe((acc^mask)|mask2,pos+1))
            return ret
        return probe(0,0)
                

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # select slots using nums, TLE
        mask=1
        mapping=[0]*len(nums)
        for i in range(len(nums)):
            mapping[i]=mask
            mask=mask<<1
        import functools
        @functools.lru_cache(None)
        def probe(acc,pos):
            if pos>numSlots:
                return 0
            ret=0
            ret=probe(acc,pos+1)
            for i in range(len(nums)):
                if nums[i]&pos and mapping[i]&acc==0:
                    ret=max(ret,nums[i]&pos+probe(acc|mapping[i],pos+1))
                    for j in range(i+1,len(nums)):
                        if nums[j]&pos and mapping[j]&acc==0:
                            ret=max(ret,nums[i]&pos+nums[j]&pos+probe(acc|mapping[i]|mapping[j],pos+1))
            return ret
        return probe(0,1)
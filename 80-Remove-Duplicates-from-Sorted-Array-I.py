class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos=0
        for item in nums:
            if pos<2 or item>nums[pos-2]:
                nums[pos]=item
                pos+=1
        return pos


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        pos=0
        cnt=1
        for idx in range(1,len(nums)):
            if nums[idx]==nums[pos]:
                if cnt>1:
                    continue
                else:
                    pos+=1
                    cnt+=1
                    nums[pos]=nums[idx]
            else:
                pos+=1
                cnt=1
                nums[pos]=nums[idx]
        return pos+1
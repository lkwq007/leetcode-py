class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        racc=sum(nums)
        lacc=0
        for i in range(len(nums)):
            racc-=nums[i]
            if lacc==racc:
                return i
            lacc+=nums[i]
        return -1

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # onepass
        record={}
        acc=0
        for i in range(len(nums)):
            cur=2*acc+nums[i]
            record[cur]=record.get(cur,i)
            acc+=nums[i]
        return record.get(acc,-1)

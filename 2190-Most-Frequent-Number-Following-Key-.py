class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt=[0]*1001
        ret=0
        for i in range(1,len(nums)):
            if nums[i-1]==key:
                cnt[nums[i]]+=1
                if cnt[nums[i]]>cnt[ret]:
                    ret=nums[i]
        return ret
class Solution:
    def check(self, nums: List[int]) -> bool:
        # two pass
        pivot=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                pivot=i
                break
        total=len(nums)
        for i in range(len(nums)-1):
            cur=(pivot+i)%total
            next=(pivot+i+1)%total
            if nums[cur]>nums[next]:
                return False
        return True

class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt=0
        total=len(nums)
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                cnt+=1
            if cnt>1:
                return False
        return True
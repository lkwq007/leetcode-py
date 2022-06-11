class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            lst=[]
            for i in range(len(nums)//2):
                if i%2:
                    lst.append(max(nums[i*2],nums[i*2+1])) 
                else:
                    lst.append(min(nums[i*2],nums[i*2+1])) 
            nums=lst
        return nums[0]
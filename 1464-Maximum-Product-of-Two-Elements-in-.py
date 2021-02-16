class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ret=max((nums[i]-1)*(nums[j]-1),ret)
        return ret

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_lst=[0,0]
        for item in nums:
            item-=1
            if item>max_lst[0]:
                max_lst[1]=max_lst[0]
                max_lst[0]=item
            elif item>max_lst[1]:
                max_lst[1]=item
        return max_lst[0]*max_lst[1]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_range=0
        pos=0
        total=len(nums)-1
        while pos<=max_range:
            tmp=pos+nums[pos]
            max_range=max(tmp,max_range)
            if max_range>=total:
                return True
            pos+=1
        return False

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def canGet(target):
#             if target==0:
#                 return True
#             pos=target-1
#             last=target
#             while pos>=0:
#                 if pos+nums[pos]>=target:
#                     last=pos
#                 pos-=1
#             if last<target:
#                 return canGet(last)
#             else:
#                 return False
#         return canGet(len(nums)-1)

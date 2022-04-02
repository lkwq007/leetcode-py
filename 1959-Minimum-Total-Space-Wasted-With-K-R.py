class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        rmax=[0]*len(nums)
        postfix=[0]*len(nums)
        racc0=0
        racc1=0
        for i in range(len(nums)-1,-1,-1):
            racc0=max(racc0,nums[i])
            rmax[i]=racc0
            racc1+=nums[i]
            postfix[i]=racc1
        

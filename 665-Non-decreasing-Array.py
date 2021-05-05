class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        cnt=0
        total=len(nums)
        for idx in range(0,total):
            left=-999999 if idx==0 else nums[idx-1]
            right=999999 if idx+1>=total else nums[idx+1]
            if nums[idx]>right:
                if right<left:
                    nums[idx+1]=nums[idx]
                else:
                    left=right
                cnt+=1
            if cnt>1:
                return False
        return True
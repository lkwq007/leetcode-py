class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        cnt=0
        total=len(nums)
        for idx in range(0,total-1):
            left=-999999 if idx==0 else nums[idx-1]
            right=left if idx+1>=total else nums[idx+1]
            if left>nums[idx]:
                if right>=left:
                    cnt+=1
                else:
                    return False
            if cnt>1:
                return False
        return True
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # naive way
        dup=0
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                dup=idx+1
            else:
                nums[idx]=-nums[idx]
        miss=0
        for i in range(len(nums)):
            if nums[i]>0:
                miss=i+1
                break
        return [dup,miss]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # naive way
        dup=0
        total=0
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            total+=i-idx
            if nums[idx]<0:
                dup=idx+1
            else:
                nums[idx]=-nums[idx]
        return [dup,dup+total]
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        record_left={}
        record_right={}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    if i in record_left or j in record_right:
                        return True
                    record_left[j]=i
                    record_right[i]=j
        return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num0=None
        num1=None
        for item in nums:
            if num0 is None or item<=num0:
                num0=item
            elif num1 is None or item<=num1:
                num1=item
            else:
                return True
        return False
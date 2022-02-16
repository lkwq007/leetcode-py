class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[nums[i] for i in range(0,len(nums),2)]
        odd=[nums[i] for i in range(1,len(nums),2)]
        even.sort()
        odd.sort(key=lambda x:-x)
        for i in range(0,len(nums),2):
            nums[i]=even[i//2]
        for i in range(1,len(nums),2):
            nums[i]=odd[i//2]
        return nums
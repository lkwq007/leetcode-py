class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simple way
        lst=sorted(nums)
        head=0
        second=(len(nums)+1)//2
        for i in range(len(nums)):
            if i&1:
                nums[i]=lst[second]
                second+=1
            else:
                nums[i]=lst[head]
                head+=1

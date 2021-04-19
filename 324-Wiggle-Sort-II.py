class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simple way
        lst=[0]*5001
        head=0
        tail=5000
        for item in nums:
            lst[item]+=1
        for i in range(nums):
            if i&1==0:
                while nums[head]==0:
                    head+=1
                nums[i]=head
                nums[head]-=1
            else:
                while nums[tail]==0:
                    tail-=1
                nums[i]=tail
                nums[tail]-=1
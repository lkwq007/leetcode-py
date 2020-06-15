class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        cur=0
        ptr1=0
        ptr2=n
        total=2*n
        while cur<total:
            nums[cur]=nums[ptr1]
            
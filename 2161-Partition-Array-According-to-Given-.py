class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # out-of-place
        left=[]
        right=[]
        middle=[]
        for item in nums:
            if item<pivot:
                left.append(item)
            elif item>pivot:
                right.append(item)
            else:
                middle.append(item)
        return left+middle+right
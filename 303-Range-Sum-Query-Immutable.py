class NumArray:

    def __init__(self, nums: List[int]):
        self.acc=[0]*(len(nums)+1)
        acc=0
        for idx in range(0,len(nums)):
            acc+=nums[idx]
            self.acc[idx+1]=acc

    def sumRange(self, i: int, j: int) -> int:
        return self.acc[j+1]-self.acc[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
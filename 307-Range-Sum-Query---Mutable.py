class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums[:]
    
    def update(self, i: int, val: int) -> None:
        diff=val-self.nums[i]
        self.nums[i]=val
        for idx in range(i,len(self.nums)):
            self.lst[idx]+=diff
    
    def sum(self,idx)->int:
        acc=0
        while idx>=0:
            acc+=self.nums[idx]
            idx=(idx&(idx+1))-1
        return acc
    def sumRange(self, i: int, j: int) -> int:
        return self.lst[j]-self.lst[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
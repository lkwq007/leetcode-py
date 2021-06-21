class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[0]*len(nums)
        self.lst=[0]*len(nums)
        for i in range(len(nums)):
            self.update(i,nums[i])
    
    def update(self, i: int, val: int) -> None:
        diff=val-self.nums[i]
        self.nums[i]=val
        while i<len(self.lst):
            self.lst[i]+=diff
            i=(i|(i+1))
    
    def sum(self,pos):
        ret=0
        while pos>=0:
            ret+=self.lst[pos]
            pos=((pos+1)&pos)-1
        return ret

    def sumRange(self, i: int, j: int) -> int:
        left=0 if i==0 else self.sum(i-1)
        right=self.sum(j)
        return right-left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
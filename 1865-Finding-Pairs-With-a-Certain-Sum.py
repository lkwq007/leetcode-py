class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # self.nums1=nums1
        self.nums2=nums2
        self.record1={}
        self.record2={}
        for item in nums1:
            self.record1[item]=self.record1.get(item,0)+1
        for item in nums2:
            self.record2[item]=self.record2.get(item,0)+1
        self.record1=[(k,v) for k,v in self.record1.items()]

    def add(self, index: int, val: int) -> None:
        last=self.nums2[index]
        self.record2[last]-=1
        self.nums2[index]+=val
        self.record2[last+val]=self.record2.get(last+val,0)+1

    def count(self, tot: int) -> int:
        ret=0
        for k,v in self.record1:
            ret+=v*self.record2.get(tot-k,0)
        return ret



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
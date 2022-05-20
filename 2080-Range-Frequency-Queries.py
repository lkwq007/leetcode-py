class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mapping={}
        for i,item in enumerate(arr):
            if item not in self.mapping:
                self.mapping[item]=[]
            self.mapping[item].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.mapping or right<self.mapping[value][0] or left>self.mapping[value][-1]:
            return 0
        lst=self.mapping[value]
        l=0
        r=len(self.mapping[value])
        while l<r:
            mid=l+(r-l)//2
            if lst[mid]<left:
                l=mid+1
            else:
                r=mid
        left=l
        l=0
        r=len(lst)-1
        while l<r:
            mid=l+(r-l)//2
            if lst[mid]<=right:
                l=mid+1
            else:
                r=mid
        while l>=0 and lst[l]>right:
            l-=1
        right=l
        if right<left:
            return 0
        return right-left+1
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
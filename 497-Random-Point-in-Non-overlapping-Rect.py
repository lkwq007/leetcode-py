import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        total=0
        self.lst=[0]*len(rects)
        self.rects=rects
        for idx in range(len(rects)):
            x1,y1,x2,y2=rects[idx]
            total+=(y2-y1+1)*(x2-x1+1)
            self.lst[idx]=total
        self.total=total
    
    def search(self,val):
        left=0
        right=len(self.lst)
        while left<right:
            middle=left+(right-left)//2
            if self.lst[middle]<=val:
                left=middle+1
            else:
                right=middle
        return left

    def pick(self) -> List[int]:
        idx=random.randrange(0,self.total)
        lst_idx=self.search(idx)
        offset=self.lst[lst_idx]-idx-1
        x1,y1,x2,y2=self.rects[lst_idx]
        width=x2-x1+1
        height=y2-y1+1
        return [x1+offset%width,y1+offset//width]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        self.weight=w
        acc=0
        for idx in range(len(w)):
            acc,self.weight[idx]=acc+self.weight[idx],acc
        self.total=acc
        self.weight.append(acc)
        print(self.weight)

    def pickIndex(self) -> int:
        idx=random.randint(0,self.total-1)
        left=0
        right=len(self.weight)
        while left<right:
            middle=left+(right-left)//2
            if self.weight[middle]>idx:
                right=middle
            else:
                left=middle+1
        return left-1



# Your Solution object will be instantiated and called as such:
w=[1,2,1]
record={}
for i in range(len(w)+1):
    record[i]=0
obj = Solution(w)
for i in range(0,1000):
    tmp=obj.pickIndex()
    record[tmp]+=1
print(record)
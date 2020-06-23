from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record={}
        ret=nums[0]
        for item in nums:
            record[item]=record.get(item,0)+1
        for item in nums:
            if record[item]==1:
                return item
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record=[0]*65
        for item in nums:
            if item<0:
                record[0]+=1
                item=-item
                record[0]%=3
            pos=1
            while item>0:
                record[pos]+=item&1
                item=item>>1
                record[pos]%=3
                pos+=1
        ret=0
        for pos in range(64,0,-1):
            ret=ret<<1
            ret|=record[pos]
        if record[0]:
            ret=-ret
        return ret
x=Solution()
x.singleNumber([0,1,0,1,0,1,99])
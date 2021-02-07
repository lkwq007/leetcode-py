class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        record=[0]*101
        for item in nums:
            record[item]+=1
        ret=0
        for i in range(len(record)):
            if record[i]==1:
                ret+=i
        return ret

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        record=[0]*101
        ret=0
        for item in nums:
            if record[item]==0:
                ret+=item
            elif record[item]==1:
                ret-=item
            record[item]+=1
        return ret
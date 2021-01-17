class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        record={}
        ret=0
        for i in range(len(nums)):
            for j in range(i):
                total=nums[i]*nums[j]
                if total in record:
                    ret+=record[total]*8
                record[total]=record.get(total,0)+1
        return ret
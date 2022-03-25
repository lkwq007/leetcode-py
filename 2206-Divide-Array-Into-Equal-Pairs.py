class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        for k,v in record.items():
            if v%2:
                return False
        return True
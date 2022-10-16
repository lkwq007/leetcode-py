class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        record={}
        ret=-1
        for item in nums:
            if item%2==0:
                record[item]=record.get(item,0)+1
                ret=item
        for k,v in record.items():
            if v>record[ret] or v==record[ret] and k<ret:
                ret=k
        return ret
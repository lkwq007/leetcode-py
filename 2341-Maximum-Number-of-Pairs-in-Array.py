class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        record={}
        r0=0
        r1=0
        for item in nums:
            record[item]=record.get(item,0)+1
        for k,v in record.items():
            r0+=v//2
            r1+=v%2
        return [r0,r1]
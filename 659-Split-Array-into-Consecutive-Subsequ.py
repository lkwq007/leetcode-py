class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort()
        for key in keys:
            cur=record[key]
            if record.get(key-2,0)+record.get(key+2,0)<cur
        return True
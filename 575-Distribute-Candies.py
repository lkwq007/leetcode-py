class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        record={}
        for item in candies:
            record[item]=record.get(item,0)+1
        num=len(candies)//2
        keys=list(record.keys())
        if len(keys)>=num:
            return num
        else:
            return len(keys)
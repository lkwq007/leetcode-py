class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        record=set()
        ret=0
        for item in nums:
            if item-diff in record and item-diff-diff in record:
                ret+=1
            record.add(item)
        return ret
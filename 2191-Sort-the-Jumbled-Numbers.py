class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            if item not in record:
                acc=0
                for x in str(item):
                    acc*=10
                    acc+=mapping[int(x)]
                record[item]=acc
        nums.sort(key=lambda x:record[x])
        return nums
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        record={}
        for item in nums1:
            record[item]=1
        for item in nums2:
            record[item]=record.get(item,0)|2
        for item in nums3:
            record[item]=record.get(item,0)|4
        return [k for k,v in record.items() if v not in (1,2,4)]
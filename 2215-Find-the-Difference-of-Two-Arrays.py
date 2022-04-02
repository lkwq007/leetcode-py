class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        record1={}
        record2={}
        for item in nums1:
            record1[item]=record1.get(item,0)+1
        for item in nums2:
            record2[item]=record2.get(item,0)+1
        ret=[[k for k,v in record1.items() if k not in record2],
        [k for k,v in record2.items() if k not in record1]]
        return ret
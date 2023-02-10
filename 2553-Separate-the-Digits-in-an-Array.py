class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret=[]
        for item in nums:
            for d in str(item):
                ret.append(int(d))
        return ret
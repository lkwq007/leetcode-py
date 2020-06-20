class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)<1:
            return []
        # sorted integer array without duplicates
        ret=[[nums[0],nums[0]]]
        for item in nums[1:]:
            if item-1==ret[-1][1]:
                ret[-1][1]=item
            else:
                ret.append([item,item])
        return list(map(lambda x: str(x[0]) if x[0]==x[1] else str(x[0])+"->"+str(x[1]),ret))
        
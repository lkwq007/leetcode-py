class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        lst=list(sorted(heights))
        ret=0
        for a,b in zip(heights,lst):
            if a!=b:
                ret+=1
        return ret
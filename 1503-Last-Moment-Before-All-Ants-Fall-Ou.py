class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left)<1:
            return n-min(right)
        if len(right)<1:
            return max(left)
        return max(max(left),n-min(right))
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        total=len(arr)
        left=total//20
        return sum(arr[left:-left])/(total-left-left)
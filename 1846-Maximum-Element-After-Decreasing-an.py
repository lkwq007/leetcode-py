class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        # 1 <= arr[i] <= 10^9
        cur=0
        for item in arr:
            cur+=1
            cur=min(cur,item)
        return cur
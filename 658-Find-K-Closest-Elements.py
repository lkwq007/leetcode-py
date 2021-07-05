class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst=[(abs(item-x),item) for item in arr]
        lst.sort()
        return sorted(map(lambda x:x[1],lst[:k]))
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def search(left,right):
            
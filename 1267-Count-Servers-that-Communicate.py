class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # three pass, O(1) space
        row=[sum(item) for item in grid]
        col=[sum(item) for item in zip(grid)]

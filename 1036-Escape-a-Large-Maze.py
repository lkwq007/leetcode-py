class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # 0 <= blocked.length <= 200, it's impossible to block all paths
        # so we only need to check whethter source and target are surrouned by blocks
        
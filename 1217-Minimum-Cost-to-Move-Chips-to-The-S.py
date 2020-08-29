class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd=0
        for item in chips:
            odd+=item&1
        return min(odd,len(chips)-odd)
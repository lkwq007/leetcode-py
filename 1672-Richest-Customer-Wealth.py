class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(item) for item in accounts])
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # distinct numbers,
        min_row=[min(row) for row in matrix]
        for 
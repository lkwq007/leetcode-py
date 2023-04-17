class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(map(lambda x:len(str(x)),row)) for row in zip(*grid)]
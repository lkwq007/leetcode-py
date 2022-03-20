class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        base=ord("a")
        record=[[] for _ in range(26)]
        
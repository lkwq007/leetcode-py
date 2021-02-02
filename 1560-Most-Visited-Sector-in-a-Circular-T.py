class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start=rounds[0]
        end=rounds[-1]
        if end<start:
            return [x for x in range(1,end+1)]+[x for x in range(start,n+1)]
        return [x for x in range(start,end+1)]
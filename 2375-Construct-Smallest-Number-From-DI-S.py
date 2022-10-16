class Solution:
    def smallestNumber(self, pattern: str) -> str:
        edges=[{} for _ in range(len(pattern)+1)]
        for i in range(len(pattern)):
            if pattern[i]=="I":
                edges[i].append(i+1)
            else:
                edges[i+1].append(i)
        
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score=[0]*len(edges)
        for i in range(len(edges)):
            score[edges[i]]+=i
        return max(score)
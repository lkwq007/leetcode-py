class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return [score[idx] for _,idx in sorted([(-score[idx][k],idx) for idx in range(len(score))])]
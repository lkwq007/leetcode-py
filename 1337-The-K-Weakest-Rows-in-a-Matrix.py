class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # brute force
        power=list(map(sum,mat))
        idx=list(range(len(mat)))
        idx.sort(key=lambda x: (power[x],x))
        return idx[:k]
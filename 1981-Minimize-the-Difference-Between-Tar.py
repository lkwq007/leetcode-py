class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 1 <= m, n <= 70, brute force?
        # 1 <= mat[i][j] <= 70
        h=len(mat)
        w=len(mat[0])
        record={}
        record[target]=1
        for y in range(h):
            tgt={}
            acc=None
            for x in range(w):
                for key in record.keys():
                    cur=key-mat[y][x]
                    if cur>=0:
                        tgt[cur]=1
                    elif acc is None or acc<cur:
                        acc=cur
            if acc is not None:
                tgt[acc]=1
            record=tgt
        return min(map(abs,record.keys()))
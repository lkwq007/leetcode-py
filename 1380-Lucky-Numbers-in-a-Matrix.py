class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # distinct numbers,
        h=len(matrix)
        w=len(matrix[0])
        min_row=[min(row) for row in matrix]
        ret=[]
        for x in range(w):
            max_idx=0
            for y in range(h):
                if matrix[max_idx][x]<matrix[y][x]:
                    max_idx=y
            if matrix[max_idx][x]==min_row[max_idx]:
                ret.append(min_row[max_idx])
        return ret

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # distinct numbers,
        min_row=set([min(row) for row in matrix])
        max_col=set([max(col) for col in zip(matrix)])
        return min_row.intersection(max_col)

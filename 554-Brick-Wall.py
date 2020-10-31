class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        record={}
        max_val=0
        for row in wall:
            acc=0
            for offset in row[:-1]:
                acc+=offset
                record[acc]=record.get(acc,0)+1
                max_val=max(max_val,record[acc])
        return len(wall)-max_val
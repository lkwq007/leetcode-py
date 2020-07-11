class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        record={"X":0,"O":0," ":0}
        for y in range(3):
            for x in range(3):
                record[board[y][x]]+=1
        if record["X"]!=record["O"] or record["X"]-1!=record["O"]:
            return False
        cnt=0
        for y in range()
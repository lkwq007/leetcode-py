class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board=[0]*9
        def is_draw():
            return sum(map(abs,board))==9
        def is_win(target):
            for y in range(3):
                acc1=0
                acc2=0
                for x in range(3):
                    acc1+=board[y*3+x]
                    acc2+=board[x*3+y]
                if acc1==target or acc2==target:
                    return True
            if board[0]+board[4]+board[8]==target or board[2]+board[4]+board[6]==target:
                return True
            return False
        chess=1
        for y,x in moves:
            board[y*3+x]=chess
            chess=-chess
        if is_win(3):
            return "A"
        if is_win(-3):
            return "B"
        if is_draw():
            return "Draw"
        return "Pending"

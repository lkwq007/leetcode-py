class Solution:
    def totalNQueens(self, n: int) -> int:
        self.acc=0
        def probe(i,lst):
            if i==n:
                self.acc+=1
                return
            conflict={}
            for idx in range(i):
                conflict[lst[idx]]=1
                conflict[lst[idx]+(i-idx)]=1
                conflict[lst[idx]-(i-idx)]=1
            for idx in range(n):
                if idx not in conflict:
                    lst[i]=idx
                    probe(i+1,lst)
        total=0
        board=[0]*n
        for i in range(n//2):
            board[0]=i
            self.acc=0
            probe(1,board)
            total+=self.acc
        total*=2
        if n%2==1:
            board[0]=n//2
            self.acc=0
            probe(1,board)
            total+=self.acc
        return total
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret=[]
        def probe(i,lst):
            if i==n:
                ret.append(lst[:])
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
        probe(0,[0]*n)
        template=["."]*n
        def convert(sol):
            ret=[]
            for i in range(n):
                template[sol[i]]="Q"
                ret.append("".join(template))
                template[sol[i]]="."
            return ret
        return list(map(convert,ret))
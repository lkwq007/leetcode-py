class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 1 <= m, n <= 300
        m=len(matrix)
        n=len(matrix[0])
        record={}
        ret=0
        x=n
        mask_lst=[]
        while x>0:
            if x>=64:
                mask_lst.append((1<<64)-1)
                x-=64
            else:
                mask_lst.append((1<<x)-1)
                x=0
        for i in range(m):
            acc=0
            cnt=0
            lst=[]
            for j in range(n):
                acc=acc*2+matrix[i][j]
                cnt+=1
                if cnt==64:
                    lst.append(acc)
                    acc=0
                    cnt=0
            if cnt>0:
                lst.append(acc)
            lst=tuple(lst)
            record[lst]=record.get(lst,0)+1
        def rev(x):
            return tuple((~x[i])&mask_lst[i] for i in range(len(x)))
        for k in record.keys():
            ret=max(ret,record[k]+record.get(rev(k),0))
        return ret
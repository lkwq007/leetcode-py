class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        h=len(matrix)
        w=len(matrix[0])
        record={}
        for y in range(h):
            for x in range(w):
                val=matrix[y][x]
                if val not in record:
                    record[val]=[]
                record[val].append((y,x))
        keys=sorted(record.keys())
        row=[0]*h
        col=[0]*w
        def find(lst,idx):
            pos=idx
            while lst[idx]!=-1:
                idx=lst[idx]
            while lst[pos]!=-1:
                tmp=lst[pos]
                lst[pos]=idx
                pos=tmp
            return idx
        def union(lst,a,b):
            ia=find(lst,a)
            ib=find(lst,b)
            if ia!=ib:
                lst[ib]=ia
            return ia
        for key in keys:
            total=len(record[key])
            disjoint=[-1]*total
            candidate=[1]*total
            row_idx=[-1]*h
            col_idx=[-1]*w
            for i in range(total):
                y,x=record[key][i]
                row_last=row[y]
                col_last=col[x]
                rc_last=max(row_last,col_last)+1
                if row_idx[y]!=-1:
                    rc_last=max(rc_last,candidate[find(disjoint,row_idx[y])])
                    reti=union(disjoint,row_idx[y],i)
                    candidate[reti]=rc_last
                if col_idx[x]!=-1:
                    rc_last=max(rc_last,candidate[find(disjoint,col_idx[x])])
                    reti=union(disjoint,col_idx[x],i)
                    candidate[reti]=rc_last
                row_idx[y]=i
                col_idx[x]=i
                candidate[i]=rc_last
                candidate[find(disjoint,i)]=rc_last
            for i in range(total):
                y,x=record[key][i]
                val=find(disjoint,i)
                val=candidate[val]
                matrix[y][x]=val
                row[y]=val
                col[x]=val
        return matrix
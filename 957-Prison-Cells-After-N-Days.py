class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        next=cells[:]
        buffer=[0]*8
        next[0]=0
        next[-1]=0
        period=0
        table=[]
        record={}
        def convert(lst):
            acc=0
            for idx in range(1,7):
                acc=lst[idx]+acc<<1
            return acc
        def to_lst(num):
            ret=[0]*8
            num=num>>1
            for idx in range(6,0,-1):
                ret[idx]=num&1
                num=num>>1
            return ret
        for i in range(N):
            for idx in range(1,7):
                next[idx]=1-(cells[idx-1]^cells[idx+1])
            num=convert(next)
            if num in record:
                base=record[num]
                period=i-base
                rest=N-1-i
                return to_lst(table[base+rest%period])
            else:
                table.append(num)
                record[num]=i
            tmp=cells
            cells=next
            next=tmp
            next[0]=0
            next[-1]=0
        return cells
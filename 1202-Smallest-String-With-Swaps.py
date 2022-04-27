class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjoint=[-1]*len(s)
        slst=list(s)
        def find(x):
            ret=x
            while disjoint[ret]>-1:
                ret=disjoint[ret]
            while disjoint[x]>-1:
                tmp=disjoint[x]
                disjoint[x]=ret
                x=tmp
            return ret
        for u,v in pairs:
            ui=find(u)
            vi=find(v)
            if ui!=vi:
                if disjoint[vi]<disjoint[ui]:
                    ui,vi=vi,ui
                disjoint[ui]+=disjoint[vi]
                disjoint[vi]=ui
        record={}
        for i in range(len(s)):
            idx=find(i)
            if idx<0:
                cur=i
            else:
                cur=idx
            if cur not in record:
                record[cur]=[]
            record[cur].append(i)
        for k,lst in record.items():
            lst.sort()
            vlst=[s[i] for i in lst]
            vlst.sort()
            for i in range(len(lst)):
                slst[lst[i]]=vlst[i]
        return "".join(slst)
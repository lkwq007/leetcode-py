class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        first={}
        second={}
        graph0={}
        graph1={}
        for a,b in pairs:
            first[a]=first.get(a,0)+1
            second[b]=second.get(b,0)+1
            if a not in graph0:
                graph0[a]={}
            if b not in graph1:
                graph1[b]={}
            graph0[a][b]=1
            graph1[b][a]=1
        start=None
        for k in first.keys():
            if first[k]>second.get(k,0):
                start=k
                break
        end=None
        for k in second.keys():
            if second[k]>first.get(k,0):
                end=k
                break
        ret=[]
        if start is None:
            # circle, pick any node
            if start is None:
                start=pairs[0][0]
            cur=start
            while len(ret)<len(pairs):
                keys=graph0[cur].keys()
                for k in keys:
                    del graph0[cur][k]
                    ret.append([cur,k])
                    cur=k
                    break
        else:
            cur=start
            pairs.append([end,start])
            if end not in graph0:
                graph0[end]={}
            graph0[end][start]=1
            cut=0
            idx=0
            while len(ret)<len(pairs):
                keys=graph0[cur].keys()
                for k in keys:
                    del graph0[cur][k]
                    ret.append([cur,k])
                    if (cur,k)==(end,start):
                        cut=idx
                    cur=k
                    break
                idx+=1
            ret=ret[cut+1:]+ret[:cut]
        return ret
                

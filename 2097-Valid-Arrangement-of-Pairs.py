from collections import deque
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        first={}
        second={}
        graph0={}
        for a,b in pairs:
            first[a]=first.get(a,0)+1
            second[b]=second.get(b,0)+1
            if a not in graph0:
                graph0[a]={}
            graph0[a][b]=1
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
        if start is not None:
            pairs.append([end,start])
            if end not in graph0:
                graph0[end]={}
            graph0[end][start]=1
            cur=start
        else:
            cur=pairs[0][0]
        record={}
        cnt=0
        lst=[]
        while cnt<len(pairs):
            keys=graph0[cur].keys()
            if keys:
                for k in keys:
                    del graph0[cur][k]
                    lst.append([cur,k])
                    cur=k
                    cnt+=1
                    break
            else:
                for k in graph0.keys():
                    cur=k
                    break
                if (lst[0][0],lst[-1][-1]) not in record:
                    record[(lst[0][0],lst[-1][-1])]=deque([])
                record[(lst[0][0],lst[-1][-1])].append(lst)
                lst=[]
        if lst:
            if (lst[0][0],lst[-1][-1]) not in record:
                record[(lst[0][0],lst[-1][-1])]=deque([])
            record[(lst[0][0],lst[-1][-1])].append(lst)
        print(record)
        def process(lst,insert=None):
            last=None
            for a,b in insert:
                if last and (last,a) in record:
                    queue=record.get((last,a),[])
                    if queue:
                        tmp=queue.pop()
                        if len(queue)==0:
                            del record[(last,a)]
                        process(lst,tmp)
                    else:
                        del record[(last,a)]
                lst.append((a,b))
                last=b
        for k in list(record.keys()):
            v=record.get(k,[])
            for i in range(len(v)):
                acc=[]
                if v:
                    cur=v.pop()
                    process(acc,cur)
                    v.appendleft(acc)
            if v:
                record[k]=v
        print(list(record.values()))
        ret=list(record.values())[0][0]
        if start is not None:
            for i in range(len(ret)):
                if ret[i]==(end,start):
                    break
            ret=ret[(i+1):]+ret[:i]
        return ret
                

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue=[1]
        record={}
        record[1]=0
        step=0
        ret=-1
        flag=False
        while queue:
            target=[]
            step+=1
            for item in queue:
                if flag:
                    break
                for next in graph[item]:
                    if next not in record:
                        record[next]=step
                        target.append(next)
                    elif record[next]+1==step:
                        target.append(next)
                    if next==n:
                        del record[n]
                        if ret==-1:
                            ret=step
                        elif ret!=step:
                            if ret+1==step:
                                flag=True
                            target=[]
                            break
            queue=target
            # print(queue)
        def process(x):
            acc=0
            cur=0
            red=False
            for i in range(x):
                acc+=time
                cur+=time
                if (cur//change)%2 and i!=x-1:
                    acc+=change-(cur%change)
                    cur=0
                else:
                    cur=cur%change
                # print(i,cur,acc)
            return acc
        if flag:
            return process(ret+1)
        else:
            return process(ret+2)
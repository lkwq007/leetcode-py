class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # at most 26
        record={}
        graph={}
        base=ord("a")
        for item in ideas:
            record[item]=1
        for item in ideas:
            head=item[0]
            if head not in graph:
                graph[head]={}
            for i in range(26):
                cur=chr(base+i)
                if cur+item[1:] not in record:
                    graph[head][cur]=graph[head].get(cur,0)+1            
        ret=0
        for item in ideas:
            head=item[0]
            tail=item[1:]
            for i in range(26):
                cur=chr(base+i)
                tmp=cur+tail
                if tmp not in record:
                    if cur in graph:
                        ret+=graph[cur].get(head,0)
        return ret
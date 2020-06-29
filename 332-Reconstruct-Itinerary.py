from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph={}
        total=len(tickets)
        for src,dst in tickets:
            if src not in graph:
                graph[src]={}
            graph[src][dst]=graph[src].get(dst,0)+1
        # dfs and backtraking
        def dfs(node,used):
            if node not in graph:
                if used==total:
                    return True,[node]
                else:
                    return False,[]
            else:
                cnt=0
                keys=list(graph[node].keys())
                keys.sort()
                for key in keys:
                    if graph[node][key]>0:
                        cnt+=1
                        graph[node][key]-=1
                        ret=dfs(key,used+1)
                        if ret[0]:
                            ret[1].append(node)
                            return True,ret[1]
                        graph[node][key]+=1
                if cnt==0 and used==total:
                    return True,[node]
                return False,[]
        ret=dfs("JFK",0)
        return list(reversed(ret[1]))
x=Solution()
print(x.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
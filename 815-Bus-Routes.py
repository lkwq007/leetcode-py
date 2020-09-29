class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S==T:
            return 0
        visited=[False]*len(routes)
        graph={}
        for i,route in enumerate(routes,0):
            for stop in route:
                if stop not in graph:
                    graph[stop]=[]
                graph[stop].append(i)
        queue=[S]
        step=0
        while queue:
            target=[]
            step+=1
            for stop in queue:
                for bus in graph[stop]:
                    if not visited[bus]:
                        visited[bus]=True
                        for next in routes[bus]:
                            if next==T:
                                return step
                            target.append(next)
            queue=target
        return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # TLE
        if S==T:
            return 0
        graph={}
        for i,route in enumerate(routes,0):
            for stop in route:
                if stop not in graph:
                    graph[stop]=[]
                graph[stop].append(i)
        queue=[S]
        d={S:0}
        step=0
        while queue:
            target=[]
            step+=1
            for stop in queue:
                for bus in graph[stop]:
                    for next in routes[bus]:
                        if next==T:
                            return step
                        if next not in d:
                            d[next]=step
                            target.append(next)
            queue=target
        return -1

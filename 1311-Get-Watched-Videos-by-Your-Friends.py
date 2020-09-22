class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue=[id]
        target=[]
        visited=[False]*len(watchedVideos)
        visited[id]=True
        for idx in range(level):
            for u in queue:
                for v in friends[u]:
                    if not visited[v]:
                        target.append(v)
                        visited[v]=True
            queue=target
            target=[]
            if len(queue)<1:
                break
        record={}
        for item in queue:
            for vid in watchedVideos[item]:
                record[vid]=record.get(vid,0)+1
        ret=[(freq,vid) for vid,freq in record.items()]
        ret.sort()
        return [item[1] for item in ret]

# wrong answer
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue=[id]
        target=[]
        visited=[False]*len(watchedVideos)
        for idx in range(level):
            for u in queue:
                visited[u]=True # if we use this flag, the bfs would be broken
                for v in friends[u]:
                    if not visited[v]:
                        target.append(v)
                        # visited[v]=True
            queue=target
            target=[]
            if len(queue)<1:
                break
        record={}
        queue=set(queue)
        for item in queue:
            for vid in watchedVideos[item]:
                record[vid]=record.get(vid,0)+1
        ret=[(freq,vid) for vid,freq in record.items()]
        ret.sort()
        return [item[1] for item in ret]

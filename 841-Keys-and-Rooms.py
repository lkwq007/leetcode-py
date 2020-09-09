class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.cnt=0
        visited=[False]*len(rooms)
        def dfs(idx):
            visited[idx]=True
            self.cnt+=1
            for key in rooms[idx]:
                if not visited[key]:
                    dfs(key)
        dfs(0)
        return self.cnt==len(rooms)
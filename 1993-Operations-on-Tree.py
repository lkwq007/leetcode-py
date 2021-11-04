class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent=parent
        self.locks=[-1]*len(parent)
        self.child=[[] for _ in range(len(parent))]
        for i in range(len(parent)):
            par=parent[i]
            if par!=-1:
                self.child[par].append(i)
        # print(self.child)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num]==-1:
            self.locks[num]=user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num]==user:
            self.locks[num]=-1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def dfs(x):
            if self.locks[x]!=-1:
                return 1
            for item in self.child[x]:
                if dfs(item)>0:
                    return 1
            return 0
        def dfs_unlock(x):
            self.locks[x]=-1
            for item in self.child[x]:
                dfs_unlock(item)
        if self.locks[num]==-1:
            cur=num
            while cur!=-1:
                if self.locks[cur]!=-1:
                    return False
                cur=self.parent[cur]
            if dfs(num)==0:
                return False
            dfs_unlock(num)
            self.locks[num]=user
            return True
        return False

                
                


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
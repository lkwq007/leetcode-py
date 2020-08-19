class RecentCounter:

    def __init__(self):
        self.lst=[]
        self.idx=0

    def ping(self, t: int) -> int:
        if len(self.lst)<1:
            self.lst.append(t)
            return 1
        self.lst.append(t)
        t_start=t-3000
        while self.lst[self.idx]<t_start:
            self.idx+=1
        return len(self.lst)-self.idx

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
import random
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        # item in blacklist are unique
        self.N=N
        self.total=N-len(blacklist)
        lower={}
        upper={}
        for item in blacklist:
            if item>=self.total:
                upper[item]=1
            else:
                lower[item]=1
        cur=self.total
        for key in lower:
            while cur in upper:
                cur+=1
            lower[key]=cur
            cur+=1
        self.mapping=lower

    def pick(self) -> int:
        choice=random.randrange(0,self.total)
        if choice in self.mapping:
            return self.mapping[choice]
        return choice


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        cnt=[0]*len(persons)
        acc=0
        self.record=[]
        for p,t in zip(persons,times):
            cnt[p]+=1
            if cnt[p]>=cnt[acc]:
                acc=p
            self.record.append((t,acc))

    def q(self, t: int) -> int:
        left=0
        right=len(self.record)-1
        while left<right:
            middle=left+(right-left)//2
            val,p=self.record[middle]
            if val==t:
                return p
            elif val<t:
                left=middle+1
            else:
                right=middle
        if self.record[left][0]>t:
            return self.record[left-1][1]
        return self.record[left][1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
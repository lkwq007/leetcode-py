class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp=[set([]) for _ in range(2501)]
        mask=1
        for item in rods:
            dp[item].add(mask)
            mask=mask<<1
        ret=0
        def count(idx):
            lst=list(dp[idx])
            for i in range(len(lst)):
                for j in range(i+1,len(lst)):
                    if lst[i]&lst[j]==0:
                        return True
            return False
        total=sum(rods)
        for i in range(1,total):
            for j in range(1,i):
                for x in dp[j]:
                    for y in dp[i-j]:
                        if x&y==0:
                            dp[i].add(x|y)
            if count(i):
                ret=i
        return ret


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # only 1000, brute force
        idx=list(range(len(scores)))
        idx.sort(key=lambda x:(ages[x],scores[x]))
        ret=0
        dp=[0]*len(scores)
        for i in range(len(idx)):
            cur=idx[i]
            dp[i]=scores[cur]
            for j in range(i):
                prev=idx[j]
                if ages[prev]<ages[cur] and scores[prev]>scores[cur]:
                    continue
                dp[i]=max(dp[i],scores[cur]+dp[j])
            ret=max(ret,dp[i])
        return ret
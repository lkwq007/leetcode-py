class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dynamic programming
        pairs.sort(key=lambda x:(x[1],x[0]))
        dp=[1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy
        pairs.sort(key=lambda x:(x[1],x[0]))
        ret=1
        last=pairs[0][1]
        for a,b in pairs:
            if last<a:
                ret+=1
                last=b
        return ret
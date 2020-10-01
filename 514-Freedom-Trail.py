class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # DP
        record={}
        for idx,item in enumerate(ring,0):
            if item not in record:
                record[item]=[]
            record[item].append(idx)
        template=[-1]*len(ring)
        total=len(ring)
        dp=[template[:] for _ in range(len(key))]
        ret=len(key)*(len(ring)+1)
        for idx in record[key[0]]:
            dp[0][idx]=min((0-idx+total)%total,(idx-0+total)%total)
        for i in range(1,len(key)):
            if key[i]==key[i-1]:
                for idx in record[key[i]]:
                    dp[i][idx]=dp[i-1][idx]
                continue
            for idx in record[key[i]]:
                for last in record[key[i-1]]:
                    tmp=min((last-idx+total)%total,(idx-last+total)%total)+dp[i-1][last]
                    if dp[i][idx]==-1:
                        dp[i][idx]=tmp
                    else:
                        dp[i][idx]=min(dp[i][idx],tmp)
        for idx in record[key[-1]]:
            ret=min(dp[-1][idx],ret)
        return ret+len(key)

# import functools
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         # TLE
#         record={}
#         for idx,item in enumerate(ring,0):
#             if item not in record:
#                 record[item]=[]
#             record[item].append(idx)
#         self.ret=len(key)*(len(ring)+1)
#         total=len(ring)
#         @functools.lru_cache(maxsize=None)
#         def dfs(pos,cur,acc):
#             while pos<len(key):
#                 if key[pos]==ring[cur]:
#                     acc+=1
#                     pos+=1
#                 else:
#                     for idx in record[key[pos]]:
#                         dfs(pos+1,idx,acc+1+min((cur-idx+total)%total,(idx-cur+total)%total))
#                     break
#             if pos==len(key):
#                 self.ret=min(self.ret,acc)
#                 return
#         dfs(0,0,0)
#         return self.ret

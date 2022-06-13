class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k==len(jobs):
            return max(jobs)
        # using dp
        mask=1
        mapping=[0]*len(jobs)
        for i in range(len(jobs)):
            mapping[i]=mask
            mask=mask<<1
        full=mask-1
        cost=[0]*mask
        for i in range(len(jobs)):
            mask=mapping[i]
            for j in range(mask):
                cost[j|mask]=cost[j]+jobs[i]
        total=sum(jobs)
        import functools
        @functools.lru_cache(None)
        def probe(mask,rest):
            if rest==1:
                return cost[mask]
            sub=mask
            ret=total
            while sub>0:
                sub=(sub-1)&mask
                cur=cost[sub^mask]
                if cur>ret:
                    continue
                tmp=probe(sub,rest-1)
                ret=min(ret,max(cur,tmp))
            return ret
        return probe(full,k)

# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
#         if k==len(jobs):
#             return max(jobs)
#         # using dp
#         mask=1
#         mapping=[0]*len(jobs)
#         for i in range(len(jobs)):
#             mapping[i]=mask
#             mask=mask<<1
#         full=mask-1
#         template=[sum(jobs)]*mask
#         dp=[template[:] for _ in range(k)]
#         dp[0][0]=0
#         for i in range(len(jobs)):
#             mask=mapping[i]
#             for j in range(mask):
#                 dp[0][j|mask]=dp[0][j]+jobs[i]
#         for i in range(1,k):
#             for mask in range(1,full+1):
#                 sub=mask
#                 while sub>0:
#                     sub=(sub-1)&mask
#                     cur=dp[0][sub] if dp[0][sub]>dp[i-1][sub^mask] else dp[i-1][sub^mask]
#                     if cur<dp[i][mask]:
#                         dp[i][mask]=cur
#         return dp[k-1][full]

# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
#         # TLE
#         if k==len(jobs):
#             return max(jobs)
#         # using dp
#         mask=1
#         mapping=[0]*len(jobs)
#         for i in range(len(jobs)):
#             mapping[i]=mask
#             mask=mask<<1
#         full=mask-1
#         template=[sum(jobs)]*mask
#         dp=[template[:] for _ in range(k)]
#         dp[0][0]=0
#         for i in range(len(jobs)):
#             mask=mapping[i]
#             for j in range(mask):
#                 dp[0][j|mask]=dp[0][j]+jobs[i]
#         for i in range(1,k):
#             for j in range(full+1):
#                 for mask in range(full+1):
#                     if j&mask==0:
#                         tmp=max(dp[0][mask],dp[i-1][j])
#                         if tmp<dp[i][j|mask]:
#                             dp[i][j|mask]=tmp
#         return dp[k-1][full]
# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
#         TLE
#         if k==len(jobs):
#             return max(jobs)
#         mapping=jobs[:]
#         mask=1
#         for i in range(len(mapping)):
#             mapping[i]=mask
#             mask=mask<<1
#         total=sum(jobs)
#         import functools
#         @functools.lru_cache(maxsize=None)
#         def probe(acc,pos):
#             if pos==k-1:
#                 cur=0
#                 for i in range(len(mapping)):
#                     if mapping[i]&acc==0:
#                         cur+=jobs[i]
#                 return cur
#             cnt=0
#             ret=0
#             for i in range(len(mapping)):
#                 if mapping[i]&acc==0:
#                     cnt+=1
#                     ret=max(jobs[i],ret)
#             if k-pos>=cnt:
#                 return ret
#             ret=total
#             for i in range(mask):
#                 cur=0
#                 if (acc&i)==acc and (acc&i)!=i:
#                     for j in range(len(mapping)):
#                         if mapping[j]&i and mapping[j]&acc==0:
#                             cur+=jobs[j]
#                     ret=min(ret,max(cur,probe(i,pos+1)))
#             return ret
#         return probe(0,0)
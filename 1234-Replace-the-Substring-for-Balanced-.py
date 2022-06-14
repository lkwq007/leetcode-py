class Solution:
    def balancedString(self, s: str) -> int:
        mapping={}
        record={}
        for i,item in enumerate("QWER"):
            mapping[item]=i
        cnt=[0]*4
        for item in s:
            cnt[mapping[item]]+=1
        need=[0]*4
        part=len(s)//4
        need=[max(0,item-part) for item in cnt]
        if sum(need)==0:
            return 0
        acc=[0]*4
        for i in range(4):
            record[(i,0)]=-1
        ret=len(s)
        for i,item in enumerate(s):
            acc[mapping[item]]+=1
            cur=i
            flag=True
            for j in range(4):
                target=acc[j]-need[j]
                if target<0:
                    flag=False
                if (j,target) in record:
                    cur=min(cur,record[j,target])
                record[(j,acc[j])]=i
            if flag:
                ret=min(ret,i-cur)
        return ret
# class Solution:
#     def balancedString(self, s: str) -> int:
#         # WA
#         mapping={}
#         record={}
#         for i,item in enumerate("QWER"):
#             mapping[item]=i
#         cnt=[0]*4
#         for item in s:
#             cnt[mapping[item]]+=1
#         need=[]
#         part=len(s)//4
#         check=[]
#         cmapping=[0]*4
#         for i in range(4):
#             if cnt[i]>part:
#                 cmapping[i]=len(check)
#                 check.append(i)
#                 need.append(cnt[i]-part)
#         if len(check)==0:
#             return 0
#         acc=[0]*len(check)
#         record[tuple(acc)]=-1
#         ret=len(s)
#         for i,item in enumerate(s):
#             if mapping[item] in check:
#                 acc[cmapping[mapping[item]]]+=1
#             target=tuple(a-b for a,b in zip(acc,need))
#             if target in record:
#                 ret=min(ret,i-record[target])
#             record[tuple(acc)]=i
#         return ret
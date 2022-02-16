class Solution:
    def uniqueLetterString(self, s: str) -> int:
        left=[-1]*26
        last=[-1]*26
        ret=0
        for i in range(len(s)):
            item=ord(s[i])-ord("A")
            if last[item]!=-1:
                ret+=(i-left[item])*last[item]
            last[item]=i-left[item]
            left[item]=i
        cur=len(s)
        for i in range(26):
            if last[i]!=-1:
                ret+=(cur-left[i])*last[i]
        return ret

# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         term=10**9+7
#         total=len(s)
#         record={}
#         acc=0
#         for i in range(0,total-1):
#             cnt=1
#             record={s[i]:1}
#             acc+=cnt
#             for j in range(i+1,total):
#                 tmp=record.get(s[j],0)+1
#                 if tmp==1:
#                     cnt+=1
#                 elif tmp==2:
#                     cnt-=1
#                 record[s[j]]=tmp
#                 acc+=cnt
#         return acc
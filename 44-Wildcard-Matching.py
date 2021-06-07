class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        template=[False]*(len(s)+1)
        dp=[template[:] for _ in range(len(p)+1)]
        dp[0][0]=True
        for i in range(len(p)):
            if p[i]=="*":
                for j in range(1+len(s)):
                    dp[i+1][j]=dp[i][j]
                for j in range(len(s)):
                    dp[i+1][j+1]=dp[i+1][j+1] or dp[i+1][j]
            else:
                for j in range(len(s)):
                    if p[i]=="?" or p[i]==s[j]:
                        dp[i+1][j+1]=dp[i][j]
        return dp[-1][-1]





class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s==p:
            return True
        p_trim=""
        last=""
        for item in p:
            if item=="*" and last=="*":
                continue
            p_trim+=item
            last=item
        p=p_trim
        def match(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if i>=len(s):
                while j<len(p):
                    if p[j]!="*":
                        return False
                    j+=1
                return True
            if s[i]==p[j] or p[j]=="?":
                return match(i+1,j+1)
            elif p[j]=="*":
                if j+1>=len(p):
                    return True
                if match(i,j+1):
                    return True
                # next=p[j+1]
                # if next!="?":
                #     while i<len(s):
                #         if s[i]==next:
                #             break
                #         i+=1
                #     return match(i,j)
                return match(i+1,j)                     
        return match(0,0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s==p:
            return True
        p_trim=""
        last=""
        for item in p:
            if item=="*" and last=="*":
                continue
            p_trim+=item
            last=item
        p=p_trim
        if p=="*":
            return True
        idx=0
        while idx<len(s) and idx<len(p):
            if p[idx].isalpha():
                if s[idx]==p[idx]:
                    idx+=1
                else:
                    return False
            else:
                break
        end=-1
        while -end<=len(s) and -end<=len(p):
            if p[end].isalpha():
                if p[end]==s[end]:
                    end-=1
                else:
                    return False
            else:
                break
        s=s[idx:end+len(s)]
        p=p[idx:end+len(p)]
        def match(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if i>=len(s):
                while j<len(p):
                    if p[j]!="*":
                        return False
                    j+=1
                return True
            if s[i]==p[j] or p[j]=="?":
                return match(i+1,j+1)
            elif p[j]=="*":
                if j+1>=len(p):
                    return True
                if match(i,j+1):
                    return True
                # next=p[j+1]
                # if next!="?":
                #     while i<len(s):
                #         if s[i]==next:
                #             break
                #         i+=1
                #     return match(i,j)
                return match(i+1,j)                     
        return match(0,0)
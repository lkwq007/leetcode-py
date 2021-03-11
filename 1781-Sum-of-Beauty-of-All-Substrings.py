class Solution:
    def beautySum(self, s: str) -> int:
        ret=0
        total=len(s)
        base=ord("a")
        for i in range(total):
            freq=[0]*26
            freq[ord(s[i])-base]=1
            for j in range(i+1,total):
                freq[ord(s[j]-base)]+=1
class Solution:
    def beautySum(self, s: str) -> int:
        ret=0
        lst=[[0]*26 for _ in range(len(s)+1)]
        base=ord("a")
        for i in range(len(s)):
            for j in range(26):
                lst[i][j]=lst[i-1][j]
            lst[i][ord(s[i])-base]+=1
        # print(lst)
        total=len(s)
        for i in range(total):
            for j in range(i+1,total):
                max_val=0
                min_val=total
                for k in range(26):
                    tmp=lst[j][k]-lst[i-1][k]
                    if tmp>0:
                        max_val=max(max_val,tmp)
                        min_val=min(min_val,tmp)                    
                # print(s[i:j+1],max_val,min_val)
                ret+=max_val-min_val
        return ret

class Solution:
    def beautySum(self, s: str) -> int:
        ret=0
        lst=[[0]*(len(s)+1) for _ in range(26)]
        base=ord("a")
        total=len(s)
        for i in range(total):
            for j in range(26):
                lst[j][i]=lst[j][i-1]
            lst[ord(s[i])-base][i]+=1
        # print(lst)
        for i in range(total):
            for j in range(i+1,total):
                max_val=0
                min_val=total
                for k in range(26):
                    tmp=lst[k][j]-lst[k][i-1]
                    if tmp>0:
                        max_val=max(max_val,tmp)
                        min_val=min(min_val,tmp)                    
                # print(s[i:j+1],max_val,min_val)
                ret+=max_val-min_val
        return ret
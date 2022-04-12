class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        nest=[]
        free=[]
        lst=[0]*len(s)
        for i in range(len(s)):
            if locked[i]=="0":
                free.append(i)
            elif s[i]=="(":
                nest.append(i)
            elif (len(nest)+len(free))==0:
                return False
            elif nest:
                idx=nest.pop()
                lst[idx]=1
                lst[i]=1
            else:
                idx=free.pop()
                lst[idx]=1
                lst[i]=1
        cnt=0
        for i in range(len(lst)-1,-1,-1):
            if lst[i]==0:
                if locked[i]=="0":
                    cnt+=1
                elif cnt==0:
                    return False
                else:
                    cnt-=1
        return True
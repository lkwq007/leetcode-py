class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointer
        if len(s)<len(t):
            return ""
        ref=[0]*64
        base=ord("A")
        for item in t:
            ref[ord(item)-base]+=1
        total=0
        for i in range(64):
            if ref[i]>0:
                total+=1
        record=[0]*64
        ret=None
        i=0
        flag=True
        left=0
        while i<len(s):
            record[ord(s[i])-base]+=1
            cnt=0
            for j in range(64):
                if record[j]>=ref[j] and ref[j]>0:
                    cnt+=1
            if total==cnt:
                while left<=i:
                    item=ord(s[left])-base
                    if record[item]>ref[item]:
                        record[item]-=1
                    else:
                        break
                    left+=1
                if ret is None or len(ret)>i+1-left:
                    ret=s[left:i+1]
            i+=1
        if ret is None:
            return ""
        return ret

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # s consists of lowercase English letters
        record=[0]*26
        base=ord("a")
        for item in s:
            record[ord(item)-base]+=1
        last=25
        next=24
        cnt=0
        ret=[]
        while last>=0 and next>=0:
            if record[last]>0:
                ret.append(chr(base+last))
                record[last]-=1
                cnt+=1
                if cnt==repeatLimit and record[last]>0:
                    cnt=0
                    next=min(next,last-1)
                    while next>=0 and record[next]==0:
                        next-=1
                    if next>=0:
                        ret.append(chr(base+next))
                        record[next]-=1
            else:
                last-=1
                cnt=0
        return "".join(ret)

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # s consists of lowercase English letters
        record=[0]*26
        base=ord("a")
        for item in s:
            record[ord(item)-base]+=1
        ret=[]
        idx=25
        next=24
        while idx>=0:
            while record[idx]>0:
                cur=min(repeatLimit,record[idx])
                record[idx]-=cur
                ret.append(chr(base+idx)*cur)
                if cur==repeatLimit and record[idx]>0:
                    next=min(next,idx-1)
                    while next>=0 and record[next]==0:
                        next-=1
                    if next>=0:
                        record[next]-=1
                        ret.append(chr(base+next))
                    else:
                        idx=-1
                        break
            idx-=1
        return "".join(ret)
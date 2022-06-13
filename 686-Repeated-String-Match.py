class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        total=len(b)+len(a)+len(a)
        prefix=[0]*len(b)
        for i in range(1,len(b)):
            j=prefix[i-1]
            while j>0 and b[i]!=b[j]:
                j=prefix[j-1]
            if b[i]==b[j]:
                j+=1
            prefix[i]=j
        pos=0
        last=0
        while pos<total:
            j=last
            while j>0 and a[pos%len(a)]!=b[j]:
                j=prefix[j-1]
            if b[j]==a[pos%len(a)]:
                j+=1
            last=j
            pos+=1
            if last==len(b):
                return (pos+len(a)-1)//len(a)
        return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ret=1
        total=(len(b)//len(a)+3)
        prefix=[0]*(len(b)+1)
        tmp=b+"#"
        for i in range(1,len(tmp)):
            j=prefix[i-1]
            while j>0 and tmp[i]!=tmp[j]:
                j=prefix[j-1]
            if tmp[i]==tmp[j]:
                j+=1
            prefix[i]=j
        pos=0
        last=prefix[-1]
        while ret<=total:
            j=last
            while j>0 and a[pos%len(a)]!=tmp[j]:
                j=prefix[j-1]
            if tmp[j]==a[pos%len(a)]:
                j+=1
            last=j
            pos+=1
            if last==len(b):
                return (pos+len(a)-1)//len(a)
            ret=(pos+len(a)-1)//len(a)
        return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        total=(len(b)+len(a)-1)//len(a)
        if b in a*total:
            return total
        if b in a*(total+1):
            return total+1
        return -1
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda x:len(x)>0,reversed(s.split(" "))))

class Solution:
    def reverseWords(self, s: str) -> str:
        lst=list(s)
        # trim
        cur=0
        pos=0
        cnt=0
        total=len(s)
        while cur<total:
            if lst[cur]!=" ":
                lst[pos]=lst[cur]
                pos+=1
                cnt+=1
            else:
                if cnt>0:
                    lst[pos]=" "
                    for i in range((cnt+1)//2):
                        lst[pos-cnt+i],lst[pos-i-1]=lst[pos-i-1],lst[pos-cnt+i]
                    pos+=1
                cnt=0
            cur+=1
        if cnt>0:
            for i in range((cnt+1)//2):
                lst[pos-cnt+i],lst[pos-i-1]=lst[pos-i-1],lst[pos-cnt+i]
        while pos>0 and lst[pos-1]==" ":
            pos-=1
        # reverse
        for i in range(0,(pos+1)//2):
            lst[i],lst[pos-i-1]=lst[pos-i-1],lst[i]
        return "".join(lst[:pos])

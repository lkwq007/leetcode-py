class Solution:
    def countAndSay(self, n: int) -> str:
        base="1"
        while n>1:
            lst=[]
            cnt=0
            last=""
            for item in base:
                if item==last:
                    cnt+=1
                else:
                    if cnt>0:
                        lst.append(str(cnt))
                        lst.append(last)
                    last=item
                    cnt=1
            if cnt>0:
                lst.append(str(cnt))
                lst.append(last)
            base="".join(lst)
            n-=1
        return base
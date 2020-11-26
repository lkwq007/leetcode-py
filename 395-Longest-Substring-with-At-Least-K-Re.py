class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k<2:
            return len(s)
        # by deleting
        self.ret=0
        def check(start,end):
            if end-start<k:
                return
            record={}
            for i in range(start,end):
                item=s[i]
                record[item]=record.get(item,0)+1
            split=[]
            for i in range(start,end):
                item=s[i]
                if record[item]<k:
                    split.append(i)
            if len(split)<1:
                self.ret=max(self.ret,end-start)
                return
            check(start,split[0])
            split.append(end)
            for i in range(len(split)-1):
                check(split[i]+1,split[i+1])
        check(0,len(s))
        return self.ret
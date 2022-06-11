class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ret=1
        def probe(pos,acc):
            if pos==len(s):
                self.ret=max(self.ret,len(acc))
                return
            for i in range(pos+1,len(s)+1):
                if s[pos:i] not in acc:
                    acc.add(s[pos:i])
                    probe(i,acc)
                    acc.remove(s[pos:i])
        probe(0,set([]))
        return self.ret
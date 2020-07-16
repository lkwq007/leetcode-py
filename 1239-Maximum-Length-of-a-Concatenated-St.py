class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks={}
        mask=1
        for i in range(ord("a"),ord("z")+1):
            masks[chr(i)]=mask
            mask=mask<<1
        lst=[]
        def convert(x):
            ret=0
            for item in x:
                mask=masks[item]
                if mask&ret:
                    return 0,0
                ret|=mask
            return ret,len(x)
        lst=list(filter(lambda x:x[0]>0,[convert(item) for item in arr]))
        if len(lst)<1:
            return 0
        total=len(lst)
        self.ret=0
        def probe(i,mask,acc):
            if i>=total:
                self.ret=max(self.ret,acc)
                return
            cur=lst[i][0]
            if cur&mask==0:
                probe(i+1,mask|cur,acc+lst[i][1])
            probe(i+1,mask,acc)
        probe(0,0,0)
        return self.ret

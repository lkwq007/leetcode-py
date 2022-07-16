class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        self.ret=[]
        def convert(x):
            hh=x>>6
            mm=x&((1<<6)-1)
            if hh<12 and mm<60:
                self.ret.append(f"{hh}:{mm:02}")
        def probe(pos,k,acc):
            if pos==10:
                if k==0:
                    convert(acc)
                return
            if k>0:
                probe(pos+1,k-1,acc*2+1)
            probe(pos+1,k,acc*2)
        probe(0,num,0)
        return self.ret
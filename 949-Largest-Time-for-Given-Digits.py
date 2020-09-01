class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        self.max=-1
        self.ret=""
        def probe(i,lst):
            if i==4:
                tmp=[A[item] for item in lst]
                hour=tmp[0]*10+tmp[1]
                minute=tmp[2]*10+tmp[3]
                if 0<=hour<=23 and 0<=minute<=59:
                    val=hour*60+minute
                    if val>self.max:
                        self.max=val
                        self.ret=f"{tmp[0]}{tmp[1]}:{tmp[2]}{tmp[3]}"
                return
            for idx in range(4):
                if idx not in lst:
                    lst.append(idx)
                    probe(i+1,lst)
                    lst.pop()
        probe(0,[])
        return self.ret
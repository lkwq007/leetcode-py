class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        acc=0
        for item in shift:
            if item[0]>0:
                acc+=item[1]
            else:
                acc-=item[1]
        total=len(s)
        acc=acc%total
        ret=""
        for idx in range(0,total):
            ret+=s[(total+idx-acc)%total]
        return ret
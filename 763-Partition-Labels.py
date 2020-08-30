class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        record={}
        for idx in range(len(S)):
            record[S[idx]]=idx
        ret=[]
        start=0
        end=record[S[0]]
        for idx in range(len(S)):
            item=S[idx]
            if idx==end:
                ret.append(end-start+1)
                start=idx+1
                end=idx+1 if idx==len(S)-1 else record[S[idx+1]]
            elif record[item]>end:
                end=record[item]
        return ret
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if len(tokens)<2:
            return 1 if len(tokens)!=0 and tokens[0]<=P else 0
        tokens.sort()
        if tokens[0]>P:
            return 0
        start=0
        end=len(tokens)-1
        ret=0
        while start<end and tokens[end]+P>tokens[start]:
            while tokens[start]<=P:
                ret+=1
                P-=tokens[start]
                start+=1
            if tokens[end]>tokens[start]:
                P+=tokens[end]
                ret-=1
                end-=1
        if start==end and P>=tokens[start]:
            ret+=1
        return ret

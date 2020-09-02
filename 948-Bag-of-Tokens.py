class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if len(tokens)<2:
            return 1 if tokens[0]<=P else 0
        tokens.sort()
        start=0
        end=len(tokens)-1
        score=0
        while start<=end:
            while start<=end and tokens[start]<=P:
                P-=tokens[start]
                start+=1
                score+=1
            if start>end:
                return score
            if tokens[end]
        
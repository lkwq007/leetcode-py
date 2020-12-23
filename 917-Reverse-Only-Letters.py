class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left=0
        S=list(S)
        right=len(S)-1
        while left<right and left<len(S) and right>=0:
            if not S[left].isalpha():
                left+=1
            if not S[right].isalpha():
                right-=1
            if S[left].isalpha() and S[right].isalpha():
                S[left],S[right]=S[right],S[left]
                left+=1
                right-=1
        return "".join(S)
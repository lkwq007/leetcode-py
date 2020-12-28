class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt=0
        vowel=set(list("aeiouAEIOU"))
        for i in range(len(s)//2):
            if s[i] in vowel:
                cnt+=1
        for i in range(len(s)//2,len(s)):
            if s[i] in vowel:
                cnt-=1
        return cnt==0
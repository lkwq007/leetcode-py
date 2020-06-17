class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s)<1 or k<1:
            return 0
        vowels=0
        template="aeiou"
        ret=0
        for idx in range(len(s)):
            left=0 if idx<k or s[idx-k] not in template else 1
            if s[idx] in template:
                vowels+=1
            vowels-=left
            ret=max(vowels,ret)
        return ret
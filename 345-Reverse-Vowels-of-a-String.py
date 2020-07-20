class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        i=0
        j=len(s)-1
        ret=list(s)
        while i<j:
            while i<j and s[i] not in vowel:
                i+=1
            while i<j and s[j] not in vowel:
                j-=1
            ret[i],ret[j]=ret[j],ret[i]
            i+=1
            j-=1
        return "".join(ret)
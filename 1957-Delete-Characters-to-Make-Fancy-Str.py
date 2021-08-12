class Solution:
    def makeFancyString(self, s: str) -> str:
        lst=list(s)
        for i in range(len(s)):
            if i>=2 and s[i]==s[i-1]==s[i-2]:
                lst[i-2]=""
        return "".join(lst)
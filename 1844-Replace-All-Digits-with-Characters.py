class Solution:
    def replaceDigits(self, s: str) -> str:
        lst=list(s)
        for i in range(1,len(s),2):
            lst[i]=chr(int(s[i])+ord(s[i-1]))
        return "".join(lst)
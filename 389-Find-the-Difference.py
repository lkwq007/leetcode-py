class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        acc=0
        for item in s:
            acc^=ord(item)
        for item in t:
            acc^=ord(item)
        return chr(acc)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        acc=0
        for idx in range(len(s)):
            acc^=ord(s[idx])^ord(t[idx])
        return chr(acc^ord(t[-1]))
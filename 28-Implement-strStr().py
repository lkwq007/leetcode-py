class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if len(needle)>len(haystack):
            return -1
        total=len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0] and haystack[i:i+total]==needle:
                return i
        return -1
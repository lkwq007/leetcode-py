class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        for idx in range(len(s)):
            if s[idx]=="6":
                break
        if idx<len(s):
            return int(s[0:idx]+"9"+s[(idx+1):])
        return num
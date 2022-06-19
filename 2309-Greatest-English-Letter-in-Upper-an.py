class Solution:
    def greatestLetter(self, s: str) -> str:
        base=ord("A")
        for i in range(25,-1,-1):
            c=chr(base+i)
            if c in s and c.lower() in s:
                return c
        return ""
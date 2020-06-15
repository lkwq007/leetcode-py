class Solution:
    def toLowerCase(self, str: str) -> str:
        ret=""
        A=ord("A")
        Z=ord("Z")
        base=ord("a")
        for item in str:
            if A<=ord(item)<=Z:
                ret+=chr(ord(item)-A+base)
            else:
                ret+=item
        return ret
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # brute force
        lst=set(letters)
        base=ord("a")
        start=ord(target)-base
        for i in range(1,26):
            item=chr(base+((start+i)%26))
            if item in lst:
                return item
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(s):
            base=ord("a")
            digits="".join(map(lambda x:str(ord(x)-base),s))
            return int(digits)
        return convert(firstWord)+convert(secondWord)==convert(targetWord)
        
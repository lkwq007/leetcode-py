class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        acc=0
        ret=[]
        for item in word:
            acc=acc*10+int(item)
            acc=acc%m
            ret.append(1 if not acc else 0)
        return ret
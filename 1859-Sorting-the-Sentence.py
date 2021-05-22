class Solution:
    def sortSentence(self, s: str) -> str:
        ret=[""]*10
        for item in s.split():
            ret[int(item[-1])]=item[:-1]
        return " ".join(ret).strip()
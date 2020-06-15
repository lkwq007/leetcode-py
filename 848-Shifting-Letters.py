class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        base=ord("a")
        char_list=list(map(lambda x: ord(x)-base,list(S)))
        total=len(shifts)
        acc=0
        for i in range(len(shifts)-1,-1,-1):
            tmp=shifts[i]
            shifts[i]+=acc
            acc+=tmp
            char=(char_list[i]+shifts[i])%26
            char_list[i]=chr(char+base)
        return "".join(char_list)

        
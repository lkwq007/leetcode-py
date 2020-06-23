class Solution:
    def reformat(self, s: str) -> str:
        digit=""
        letter=""
        for item in s:
            if item.isdigit():
                digit+=item
            else:
                letter+=item
        if abs(len(letter)-len(digit))>1:
            return ""
        if len(letter)>len(digit):
            longer=letter
            shorter=digit
        else:
            longer=digit
            shorter=letter
        ret=""
        for idx in range(len(shorter)):
            ret+=longer[idx]+shorter[idx]
        return ret+longer[len(shorter):]
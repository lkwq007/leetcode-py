class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel="aeiouAEIOU"
        words=S.split(" ")
        for idx in range(len(words)):
            word=words[idx]
            if word[0] not in vowel:
                words[idx]=word[1:]+word[0]
            words[idx]+="ma"+"a"*(idx+1)
        return " ".join(words)
class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(" "),key=lambda x:len(x))).capitalize()

class Solution:
    def arrangeWords(self, text: str) -> str:
        words=text.split(" ")
        words[0]=words[0].lower()
        words.sort(key=lambda x:len(x))
        words[0]=words[0].capitalize()
        return " ".join(words)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ret=0
        broken=set(brokenLetters)
        for word in text.split(" "):
            flag=True
            for item in word:
                if item in broken:
                    flag=False
                    break
            if flag:
                ret+=1
        return ret
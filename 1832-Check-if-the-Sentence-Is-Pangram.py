class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst=[0]*26
        base=ord("a")
        for item in sentence:
            lst[ord(item)-base]+=1
        for item in lst:
            if item==0:
                return False
        return True

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
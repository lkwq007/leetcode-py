class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        record=[0]*26
        base=ord("a")
        for item in licensePlate:
            if item.isalpha():
                record[ord(item.lower())-base]+=1
        ret=""
        for word in words:
            lst=[0]*26
            for item in word:
                lst[ord(item)-base]+=1
            flag=True
            for i in range(26):
                if record[i]>lst[i]:
                    flag=False
                    break
            if flag:
                if len(ret)==0 or len(ret)>len(word):
                    ret=word
        return ret
            
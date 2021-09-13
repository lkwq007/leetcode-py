class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=0
        while i<len(word):
            if word[i]==ch:
                break
            i+=1
        if i==len(word):
            return word
        total=i+1
        lst=list(word)
        for i in range(total//2):
            lst[i],lst[total-1-i]=lst[total-1-i],lst[i]
        return "".join(lst)
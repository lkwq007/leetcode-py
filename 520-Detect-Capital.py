class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first=1 if word[0].isupper() else 0
        rest=0
        for item in word[1:]:
            if item.isupper():
                rest+=1
        return (first==0 or first==1) and rest==0 or (first+rest==len(word))
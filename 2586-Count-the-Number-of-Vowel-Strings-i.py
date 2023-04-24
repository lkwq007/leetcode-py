class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        acc=0
        vowel=set("aeiou")
        for word in words[left:right+1]:
            if word[0] in vowel and word[-1] in vowel:
                acc+=1
        return acc
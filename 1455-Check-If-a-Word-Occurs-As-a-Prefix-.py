class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # brute force
        lst=sentence.split()
        for i in range(len(lst)):
            word=lst[i]
            if len(word)>=len(searchWord) and word[:len(searchWord)]==searchWord:
                return i+1
        return -1
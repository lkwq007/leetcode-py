class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # each word are distinct
        graph={}
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                
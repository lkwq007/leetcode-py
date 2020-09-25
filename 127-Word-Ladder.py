class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        record={}
        flag=False
        for word in wordList:
            record[word]=0
            if word==endWord:
                flag=True
        if not flag:
            return 0
        
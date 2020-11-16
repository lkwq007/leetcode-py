class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        record1={}
        record2={}
        for a,b in zip(word1,word2):
            record1[a]=record1.get(a,0)+1
            record2[b]=record2.get(b,0)+1
        process=lambda x: list(sorted(x))
        return process(record1.keys())==process(record2.keys()) and process(record1.values())==process(record2.values())
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total=len(words)
        record={}
        for word in words:
            for item in word:
                if item not in record:
                    record[item]=0
                record[item]+=1
        for k,v in record.items():
            if v%total!=0:
                return False
        return True
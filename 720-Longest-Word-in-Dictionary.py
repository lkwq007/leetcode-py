class Solution:
    def longestWord(self, words: List[str]) -> str:
        # naive idea
        words.sort()
        ret=""
        record={}
        for item in words:
            if len(item)==1:
                record[item]=1
                if len(item)>len(ret):
                    ret=item
            else:
                if item[:-1] in record:
                    record[item]=1
                    if len(item)>len(ret):
                        ret=item
        return ret
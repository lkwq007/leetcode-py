class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        record={}
        for item in chars:
            record[item]=record.get(item,0)+1
        ret=0
        for word in words:
            tmp={}
            for item in word:
                tmp[item]=tmp.get(item,0)+1
            flag=True
            for k,v in tmp.items():
                if v>record.get(k,0):
                    flag=False
                    break
            if flag:
                ret+=len(word)
        return ret
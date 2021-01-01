class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban={}
        for item in banned:
            ban[item]=1
        self.idx=0
        def eat_nonalpha():
            while self.idx<len(paragraph) and not paragraph[self.idx].isalpha():
                self.idx+=1
        def eat_alpha():
            start=self.idx
            while self.idx<len(paragraph) and paragraph[self.idx].isalpha():
                self.idx+=1
            return paragraph[start:self.idx].lower()
        record={}
        while self.idx<len(paragraph):
            eat_nonalpha()
            token=eat_alpha()
            if len(token)>0 and token not in ban:
                record[token]=record.get(token,0)+1
        ret=""
        cnt=0
        for k,v in record.items():
            if v>cnt:
                ret=k
                cnt=v
        return ret
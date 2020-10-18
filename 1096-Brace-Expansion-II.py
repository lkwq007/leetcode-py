class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.idx=0
        def eat_word():
            start=self.idx
            while self.idx<len(expression) and expression[self.idx].isalpha():
                self.idx+=1
            return expression[start:self.idx]
        def parse():
            lst=[""]
            ret=set([])
            while self.idx<len(expression):
                item=expression[self.idx]
                if item=="{":
                    self.idx+=1
                    tmp=parse()
                    new_lst=[]
                    for a in lst:
                        for b in tmp:
                            new_lst.append(a+b)
                    lst=new_lst
                elif item=="}":
                    self.idx+=1
                    break
                elif item==",":
                    self.idx+=1
                    for item in lst:
                        ret.add(item)
                    lst=[""]
                else:
                    word=eat_word()
                    for i in range(len(lst)):
                        lst[i]+=word
            if len(lst)>1 or lst[0]!="":
                for item in lst:
                    ret.add(item)
            return ret
        ret=parse()
        return list(sorted(ret))
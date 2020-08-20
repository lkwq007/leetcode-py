class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[{}]
        idx=0
        total=len(formula)
        self.idx=0
        def atom():
            start=self.idx
            self.idx+=1
            while self.idx<total and formula[self.idx].islower():
                self.idx+=1
            return formula[start:self.idx]
        def digit():
            start=self.idx
            while self.idx<total and formula[self.idx].isdigit():
                self.idx+=1
            return int(formula[start:self.idx])
        def is_digit():
            return self.idx<total and formula[self.idx].isdigit()
        while self.idx<total:
            item=formula[self.idx]
            if item=="(":
                stack.append({})
                self.idx+=1
            elif item==")":
                self.idx+=1
                if is_digit():
                    cnt=digit()
                else:
                    cnt=1
                top=stack.pop()
                for key,val in top.items():
                    stack[-1][key]=stack[-1].get(key,0)+val*cnt
            else:
                cur=atom()
                cnt=digit() if is_digit() else 1
                stack[-1][cur]=stack[-1].get(cur,0)+cnt
        record=stack[-1]
        keys=sorted(list(record.keys()))
        ret=""
        for key in keys:
            cnt=record[key]
            ret+=key
            if cnt>1:
                ret+=str(cnt)
        return ret

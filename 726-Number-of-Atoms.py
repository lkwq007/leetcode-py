class Solution:
    def countOfAtoms(self, formula: str) -> str:
        record={}
        stack=[]
        idx=0
        total=len(formula)
        while idx<total:
            item=formula[idx]
            if item.isupper():
                tmp=item
                idx+=1
                while formula[idx].islower():
                    tmp+=formula[idx]
                    idx+=1
                digit=""
                while formula[idx].isdigit():
                    digit+=formula[idx]
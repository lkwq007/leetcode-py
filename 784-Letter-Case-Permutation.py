from typing import List



class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        template_lower=list(S.lower())
        template_upper=list(S.upper())
        template=list(S.lower())
        ret=[]
        count=0
        for item in template:
            if item.isalpha():
                count+=1
        total=1<<count
        for i in range(0,total):
            cursor=1
            for idx in range(0,len(template)):
                if 
            tmp="".join(template)
            ret.append(tmp)

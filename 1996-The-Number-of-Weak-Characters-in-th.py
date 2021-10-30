class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(x[0],-x[1]))
        ret=0
        stack=[]
        for attack,defense in properties:
            while stack:
                a,d=stack[-1]
                if a<attack and d<defense:
                    ret+=1
                    stack.pop()
                else:
                    break
            stack.append((attack,defense))
        return ret
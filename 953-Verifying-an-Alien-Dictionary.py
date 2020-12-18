class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping={}
        for i,item in enumerate(order):
            mapping[item]=i
        feature=[[mapping[item] for item in word] for word in words]
        for i in range(1,len(feature)):
            if feature[i]<feature[i-1]:
                return False
        return True
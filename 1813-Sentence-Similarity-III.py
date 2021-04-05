class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        lst1=sentence1.split(" ")
        lst2=sentence2.split(" ")
        def check(l1,l2):
            left=0
            while left<len(l1) and left<len(l2) and l1[left]==l2[left]:
                left+=1
            if left==len(l1):
                return True
            right=0
            while right<len(l1) and right<len(l2) and l1[-1-right]==l2[-1-right]:
                right+=1
            if right==len(l1):
                return True
            # print(left,right)
            return len(l1)-right==left
        return check(lst1,lst2) or check(lst2,lst1)
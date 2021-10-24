class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(x):
            cnt=0
            for i in range(len(x)):
                if x[i]=="-":
                    if cnt>0 or not (i>0 and x[i-1].isalpha() and i+1<len(x) and x[i+1].isalpha()):
                        return False
                    cnt+=1
                elif x[i] in ",.!":
                    if i!=len(x)-1:
                        return False
                elif x[i].isdigit():
                    return False
            return True
        return len([item for item in sentence.split() if is_valid(item)])
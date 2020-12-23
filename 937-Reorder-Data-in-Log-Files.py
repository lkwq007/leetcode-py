class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit=[]
        letter=[]
        for log in logs:
            lst=log.split(" ")
            if lst[-1].isalpha():
                letter.append((lst[1:],lst[:1]))
            else:
                digit.append(log)
        letter.sort()
        ret=[" ".join(id+word) for word,id in letter]
        return ret+digit
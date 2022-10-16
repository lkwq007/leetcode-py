class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # brute force
        lst=list(s)
        ret=0
        while True:
            acc=0
            pos=1
            while pos<len(s):
                if lst[pos-1]=="0" and lst[pos]=="1":
                    lst[pos-1]="1"
                    lst[pos]="0"
                    acc+=1
                    pos+=1
                pos+=1
            if acc==0:
                return ret
            ret+=1
            acc=0
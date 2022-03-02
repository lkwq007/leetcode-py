class Solution:
    def minimumBuckets(self, street: str) -> int:
        # greedy
        if street=="H" or street[:2]=="HH" or street[-2:]=="HH" or "HHH" in street:
            return -1
        ret=0
        street=list(street)
        for i in range(len(street)):
            if street[i]=="H":
                if i==0 or street[i-1]!="B":
                    if i+1<len(street) and street[i+1]!="H":
                        street[i+1]="B"
                    else:
                        street[i-1]="B"
                    ret+=1
        # print(street)
        return ret


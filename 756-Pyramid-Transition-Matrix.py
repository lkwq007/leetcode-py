class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mapping={}
        first={}
        second={}
        for item in allowed:
            head=item[:2]
            if head in mapping:
                mapping[head].append(item[2])
            else:
                mapping[head]=[item[2]]
            first[item[0]]=1
            second[item[1]]=1
        bottom=list(bottom)
        for i in range(len(bottom)-1):
            for idx in range(len(bottom)-i-1):
                tmp=bottom[idx]+bottom[idx+1]
                if tmp in mapping:
                    

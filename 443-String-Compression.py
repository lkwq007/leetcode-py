class Solution:
    def compress(self, chars: List[str]) -> int:
        pos=1
        count=1
        idx=1
        total=len(chars)
        while idx<total:
            if chars[idx]==chars[idx-1]:
                count+=1
            else:
                if count>1:
                    cnt=str(count)
                    for item in cnt:
                        chars[pos]=item
                        pos+=1
                chars[pos]=chars[idx]
                pos+=1
                count=1
            idx+=1
        if count>1:
            cnt=str(count)
            for item in cnt:
                chars[pos]=item
                pos+=1
        return pos
class Solution:
    def largestPalindromic(self, num: str) -> str:
        record={}
        for item in num:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(reverse=True)
        left=""
        right=""
        middle=""
        if len(keys)==1 and keys[0]=="0":
            return "0"
        for k in keys:
            cur=record[k]
            if cur%2 and len(middle)==0:
                middle=k
            cnt=cur//2
            if not (k=="0" and len(left)==0):
                left=left+k*cnt
                right=k*cnt+right
        return left+middle+right

class Solution:
    def largestPalindromic(self, num: str) -> str:
        record={}
        for item in num:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(reverse=True)
        left=""
        right=""
        middle=""
        for k in keys:
            cur=record[k]
            if cur%2 and len(middle)==0:
                middle=k
            cnt=cur//2
            left=left+k*cnt
            right=k*cnt+right
        ret=left+middle+right
        ret=ret.strip("0")
        if ret:
            return ret
        return "0"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        for item in t:
            if item in record:
                if record[item]==0:
                    return False
                record[item]-=1
            else:
                return False
        for key in record.keys():
            if record[key]>0:
                return False
        return True
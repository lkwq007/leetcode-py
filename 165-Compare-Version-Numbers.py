class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1=list(map(int,version1.split(".")))
        lst2=list(map(int,version2.split(".")))
        if len(lst1)<len(lst2):
            lst1=lst1+[0]*(len(lst2)-len(lst1))
        else:
            lst2=lst2+[0]*(len(lst1)-len(lst2))
        for a,b in zip(lst1,lst2):
            if a>b:
                return 1
            elif a<b:
                return -1
        return 0
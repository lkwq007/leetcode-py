class Solution:
    def dayOfYear(self, date: str) -> int:
        lst=list(map(int,date.split("-")))
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        leap=1 if lst[0]%400==0 or (lst[0]%4==0 and lst[0]%100!=0) else 0
        ret=lst[2]
        for idx in range(lst[1]-1):
            ret+=month[idx]
        if lst[1]>2:
            ret+=leap
        return ret
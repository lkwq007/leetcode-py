class Solution:
    def reformatDate(self, date: str) -> str:
        dd,mm,yy=date.split(" ")
        dd=int(dd[:-2])
        lst=["","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mapping={item:i for i,item in enumerate(lst)}
        mm=mapping[mm]
        return f"{yy}-{mm:02}-{dd:02}"

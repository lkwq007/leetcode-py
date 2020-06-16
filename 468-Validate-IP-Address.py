class Solution:
    def validIPAddress(self, IP: str) -> str:
        lst=IP.split(".")
        if len(lst)==4:
            for item in lst:
                if item.isdigit() and 0<=int(item)<=255 and (len(item)>1 and item[0]!="0" or len(item)==1):
                    pass
                else:
                    return "Neither"
            return "IPv4"
        lst=IP.split(":")
        if len(lst)==8:
            for item in lst:
                if item.isalnum() and len(item)<=4 and all(map(lambda c: c.isdigit() or ord("a")<=ord(c)<=ord("f"),item.lower())):
                    pass
                else:
                    return "Neither"
            return "IPv6"
        return "Neither"
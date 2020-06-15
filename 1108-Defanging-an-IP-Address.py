class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip=address.split(".")
        return "[.]".join(ip)
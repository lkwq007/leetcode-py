class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret=set([])
        for item in emails:
            lst=item.split("@")
            local=lst[0].split("+")[0]
            local="".join(local.split("."))
            ret.add(local+"@"+lst[1])
        return len(ret)
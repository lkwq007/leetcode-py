class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping={}
        for account in accounts:
            name=account[0]
            for email in account[1:]:
                mapping[email]=name
        mail_list=list(mapping.keys())
        disjoint=[-1]*len(mail_list)
        for account in accounts:
            for email in accounts[1:]
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                return False
        special="!@#$%^&*()-+"
        return any(map(lambda x:x.isdigit(),password)) and any(
            map(lambda x:x.isupper(),password)
        ) and any(
            map(lambda x:x.islower(),password)
        ) and any(
            map(lambda x:x in special,password)
        )

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return all([
            len(password)>=8,
            *map(
                lambda f: f[1](any(map(f[0],zip(password," "+password)))),
                [
                    (lambda x:x[0]==x[1],lambda x: not x),
                    (lambda x:x[0].isdigit(),lambda x:x),
                    (lambda x:x[0].isupper(),lambda x:x),
                    (lambda x:x[0].islower(),lambda x:x),
                    (lambda x:x[0] in "!@#$%^&*()-+",lambda x:x)
                ]
            )
        ])
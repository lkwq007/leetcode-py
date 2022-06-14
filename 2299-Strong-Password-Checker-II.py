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

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        import functools
        return (functools.reduce(lambda acc,cur: functools.reduce(
                lambda a,b:a|b,
                map(
                    lambda f: f(cur),
                    [
                        lambda x:(0,1)[x[0]==x[1]],
                        lambda x:(0,2)[x[0].isdigit()],
                        lambda x:(0,4)[x[0].isupper()],
                        lambda x:(0,8)[x[0].islower()],
                        lambda x:(0,16)[x[0] in "!@#$%^&*()-+"],
                        lambda x:(0,32)[(acc>>6)>=8]
                    ]
                ),acc&63
            )+(((acc>>6)+1)<<6),
            zip(password," "+password),0)&63)==62

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        import functools
        return (functools.reduce(lambda acc,cur: functools.reduce(
                lambda a,b:a|b,
                map(
                    lambda f: f(cur),
                    [
                        lambda x:(0,1)[x[0]==x[1]],
                        lambda x:(0,2)[x[0].isdigit()],
                        lambda x:(0,4)[x[0].isupper()],
                        lambda x:(0,8)[x[0].islower()],
                        lambda x:(0,16)[x[0] in "!@#$%^&*()-+"],
                        lambda x:(0,32)[(acc>>6)>=7]
                    ]
                ),acc&63
            )+(((acc>>6)+1)<<6),
            zip(password," "+password),0)&63)==62

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        import functools
        return (functools.reduce(lambda acc,cur: functools.reduce(lambda a,b:a|b, [(0,1)[cur[0]==cur[1]], (0,2)[cur[0].isdigit()], (0,4)[cur[0].isupper()], (0,8)[cur[0].islower()], (0,16)[cur[0] in "!@#$%^&*()-+"], (0,32)[(acc>>6)>=7]],acc&63)+(((acc>>6)+1)<<6),zip(password," "+password),0)&63)==62
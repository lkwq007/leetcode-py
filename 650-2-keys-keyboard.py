class Solution:
    def minSteps(self, n: int) -> int:
        i=2
        ret=0
        while i<=n:
            if n%i==0:
                ret+=i
                n=n//i
            else:
                i=i+(1 if i==2 else 2)
        return ret
# class Solution:
#     def minSteps(self, n: int) -> int:
#         def is_prime(n):
#             i=2
#             while i*i<=n:
#                 if n%i==0:
#                     return False
#                 i+=1
#             return True
#         if n<1:
#             return 0
#         i=2
#         ret=0
#         while i<=n:
#             if is_prime(i) and n%i==0:
#                 ret+=i
#                 n=n//i
#                 i=2
#             else:
#                 if i==2:
#                     i+=1
#                 else:
#                     i+=2
#         return ret
# class Solution:
#     def minSteps(self, n: int) -> int:
#         def is_prime(n):
#             i=2
#             while i*i<=n:
#                 if n%i==0:
#                     return False
#                 i+=1
#             return True
#         def factor(n):
#             if n<4:
#                 return n
#             i=2
#             ret=0
#             while i<=n:
#                 if is_prime(i) and n%i==0:
#                     ret+=i
#                     n=n//i
#                     i=2
#                 else:
#                     i+=1
#             return ret
#         return factor(n) if n>1 else 0
        
                
def is_prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def factor(n):
    if n<4:
        return [n]
    i=2
    ret=[]
    while i*i<=n:
        if is_prime(i) and n%i==0:
            ret.append(i)
            n=n/i
            i=2
        else:
            i+=1
    return ret
print(is_prime(3))
print(is_prime(19))
print(factor(3))
print(factor(100))
print(factor(99))
def minSteps(n: int) -> int:
    def is_prime(n):
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    if n<1:
        return 0
    i=2
    ret=0
    while i<=n:
        if is_prime(i) and n%i==0:
            ret+=i
            n=n//i
            i=2
        else:
            if i==2:
                i+=1
            else:
                i+=2
    return ret
print(minSteps(1))
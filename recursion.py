
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)
    
def compareTo(s1,s2):
    if len(s1) < len(s2):
        return -1
    if len(s1) == len(s2):
        return 0
    if len(s1) > len(s2):
        return 1
    return(compareTo(s1[1:],s2[1:]))


        
    
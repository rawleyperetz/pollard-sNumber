# A code to compute the p and q using Pollard's p-1 algorithm
# Pollard's p-1 factorization

def factorialFunc(number:int) -> int:
    fact = 1
    for i in range(1,number+1):
        fact = i*fact
    return fact 

def Gcd(a,b):
    if a>b:
        a,b=b,a
        print('Next time, let the first argument be > the second argument, dumbass. The answer is still right though') 
    if a<0 or b<0:
        return 'both a and b must be positive'
    if isinstance(a,int)==True and isinstance(b,int)==True:
        while a!=0:
            a,b=b%a,a
        return b 
    else:
        return 'both a and b must be integers'

def pollardNo(n:int, a:int, k_val:int):
    k = range(1, k_val + 1)
    for exp in k:
        mod_val = (pow(a,factorialFunc(exp)) - 1)%n
        gcd_val = Gcd(mod_val, n)
        if gcd_val != 1:
            print(f"Iteration number: {exp}: Factors are {gcd_val} and {int(n/gcd_val)}")
        
print(pollardNo(1403,2,5))
print(pollardNo(2993,2,5))
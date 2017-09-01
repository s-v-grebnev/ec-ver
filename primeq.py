import random
import time
from gcd import gcd

def buildsmallprimes(c):
    sprimes = [True] * c
    for i in range(2, c):
        if sprimes[i] == True:
            for j in range(2 * i, c, i):
                sprimes[j] = False
    primes = []
    for i in range(2, c):
        if sprimes[i] == True:
            primes.append(i)
    return primes

def MR(c, k = 256):
    random.seed(time.time())
    N = c
    u = N - 1
    t = 0
    while u % 2 == 0:
        u /= 2
        t += 1
    for cnt in range(k):
        a = random.randint(1, c - 1)
        if gcd(a, c) != 1:
            return False
        a = pow(a, u, N)
        if a == 1:
            continue
        flg = False
        for i in range(t):
            if a == N - 1:
                flg = True
                continue
            a = a ** 2
        if flg == True:
            continue
        else:
            return False
    return True

smallprimes = buildsmallprimes(1000)

def primeq(c):
    for i in smallprimes:
        if c == i:
            return True
        else:
            if c %i == 0:
                return False
    return MR(c, 256)
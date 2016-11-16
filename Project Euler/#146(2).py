'''Same for the number of six prime you try to split on, but you think about what divisible by 59 for 10001-10027. Multiple of 59 of the first of more than 10001 is 10030. Therefore is not divisible 10001-10027 in 59. This consists mostly for large prime numbers. Need to divide the number of six this will not.
As for the small primes, for example when the 7 N 2 remainder of 7 is 0, 1, 2, 4. When the remainder is 0 N 2 are divisible by 7 + 7. When 1 N 2 when the 27,4 + N 2 I divisible by 7 + 3. When calculated in advance this, need to divide the number of six is eliminated.
I was in 139 seconds this.'''

from itertools import *
from math import sqrt
import time

def  Make_primes (N):
    M = (N + 1) / 2
    a = [True] * M
    G_primes = (2 * N + 1 for N in count (1) if a [N])
    for P in takewhile ( lambda P: P * P <= N, G_primes):
         for N in xrange (P * P / 2, M, p):
            a [n] = False
    
    Return [2] + [2 * N + 1 for N in xrange (1, M) if a [N]]

def  is_prime (N):
 # M = int (sqrt (N)) 
    Return all(! N% P = 0 for P in takewhile ( lambda P: P * P <= N, primes))
 # Return all (N% P ! = 0 for p in xrange (7, m + 1, 2))

def  Fermat_test (N, b):
     Return pow(b, N - 1, N) == 1

def  Is_consecutive_primes (a):
     if a [0]% 3 == 1:
         Return False
    
    for P in Small_primes:
         if a [0]% P in rs [P]:
             Return False
    
    if  not all (Fermat_test (M, 2) for M in a):
         Return False
    
    for c in cs2:
        m = a [0] - 1 + c
        if Fermat_test (M, 2) and is_prime (M):
             Return False
    
    for P in takewhile ( lambda P: P * P <= a [-1], primes):
        q = (a [0] - 1 + p) / p * p
        if Q - a [0] - 1> 27:
             Continue 
        if Q - (a [0] - 1) in cs:
             Return False
    
    Return True

def  Calc_rs ():
    rs = [set () for _ in xrange (Small_primes [-1] + 1)]
     for P in Small_primes:
         for N in xrange (P):
             if any ((N * N + c)% P == 0 for c in cs):
                rs [p]. add ((n * n + 1)% p)
    Return rs

t0 = time.clock ()
N = 15 * 10 ** 7
primes = make_primes (N)
Print time.clock () - T0
small_primes = primes [3:13]
cs = [1, 3, 7, 9, 13, 27]
cs2 = [21]
set_cs = set (cs)
rs = calc_rs ()
Print sum (N for N in xrange (10, N, 10)
             if Is_consecutive_primes ([N * N + c for c in cs]))
 Print time.clock () - T0



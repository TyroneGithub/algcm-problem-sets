fibs = [-1]*88

def fib(n):
    if n == 0:  return 1
    if n == 1:  return 1
    if n < 88:
        if fibs[n] == -1:    fibs[n] = fib(n-1) + fib(n-2)
        return fibs[n]
    return 1000000000000000001

def solve(n,k):
    if n == 0:  return 'H'
    if n == 1:  return 'A'
    if k < fib(n-2):
        if n > 88:  n = 89 #clip n
        return solve(n-2, k)
    return solve(n-1, k-fib(n-2))

n, k = list(map(int,input().rstrip().split(" ")))
print(solve(n,k))
q, n = list(map(int,input().rstrip().split(" ")))
a = [int(input().rstrip()) for i in range(n)]

MOD = 1000000007
F = [-1] * n

for i in range(n):
    if i == 0:
        F[i] = a[i] % MOD
    else:
        F[i] = (a[i] + sum(F[:i])) % MOD
    

outs = []

for i in range(q):
    k = int(input().rstrip())
    outs.append(F[k])
print("{}".format("\n".join(list(map(str,outs)))))
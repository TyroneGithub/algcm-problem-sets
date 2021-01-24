n = int(input())
sequence = [0 for ctr in range(n + 1)]
sequence[0] = 1
sequence[1] = 1

for ctr1 in range (2, n + 1) :
    sequence[ctr1] = 0
    for ctr2 in range(ctr1) :
        sequence[ctr1] += sequence[ctr2] * sequence[ctr1 - ctr2 - 1]
        sequence[ctr1] %= (int(1e9) + 7)

print(sequence[n])
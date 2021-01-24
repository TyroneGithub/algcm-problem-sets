queries = int(input().strip())
sequence = [0 for ctr in range(int(3e5) + 1)]
ans = []

sequence[0] = 1
sequence[1] = 1
sequence[2] = 2

for ctr in range(3, int(3e5) + 1) :
    sequence[ctr] = (sequence[ctr - 2] + sequence[ctr - 3]) % (int(1e9) + 7)

for ctr in range(0, queries):
    query = int(input().strip())
    ans.append(sequence[query])

for ctr in range(0, queries) :
    print(ans[ctr])
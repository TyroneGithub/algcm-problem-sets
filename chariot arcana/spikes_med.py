def solve(k, s, memo):
    MOD = int(1e9) + 7
    
    start = 0
    end = k - 1
    _sum = 1
    
    while start < end:
        spike = s.find('1', start, end)
        
        if spike != -1:
            if spike > start:
                _sum =  (_sum % MOD * jumps(spike - start - 1, memo) % MOD) % MOD
                start = spike + 1
            else:
                _sum = 0
                break
        else:
            _sum = (_sum % MOD * jumps(end - start, memo) % MOD) % MOD
            break
    
    return _sum


def jumps(k, memo):
    # number of jumps to nth square = number of jumps to n-1 + n-2
    # logic: one square left, two squares left
    # zero-based index; (k-1) at first
    
    SENTINEL = -1
    MOD = int(1e9) + 7
    
    if memo[k] != SENTINEL:
        return memo[k]
    if k <= 1:
        return 1
    else:
        memo[k] = (jumps(k - 1, memo) % MOD + jumps(k - 2, memo) % MOD) % MOD
        return memo[k]

n = int(input().rstrip())
s = input().rstrip()

SENTINEL = -1
memo = [SENTINEL] * n
print(solve(n, s, memo))
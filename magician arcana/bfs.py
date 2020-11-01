#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, AL, s):
    dist = [-1]*n
    dist[s-1] = 0
    q = [s]
    
    ctr = 1
    while len(q) > 0:
        i = q.pop(0)
        
        for k in AL[i-1]:
            if dist[k-1] == -1:
                q.append(k)
                dist[k-1] = dist[i-1] + 6
    
    dist.remove(0)
    return dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = [[] for i in range(n)]
        
        for _ in range(m):
            e = list(map(int, input().rstrip().split()))
            
            if e[1] not in edges[e[0]-1]:
                edges[e[0]-1].append(e[1])
                edges[e[1]-1].append(e[0])

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
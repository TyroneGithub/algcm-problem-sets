#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define HI 2e9

int main() {
    int ctr;
    int a, numQueries;
    int *query;
    long int lo, hi, mid;
    
    scanf("%d %d", &a, &numQueries);
    
    query = malloc(numQueries * sizeof(int));
    
    for (ctr = 0; ctr < numQueries; ctr++) {
        scanf("%d", &query[ctr]);
    }
    
    if (a > 0) {
        for (ctr = 0; ctr < numQueries; ctr++) {
            lo = 0;
            hi = HI;
            
            while (lo < hi) {
                mid = lo + (hi - lo) / 2;
                
                if (a * sin(mid) + a * mid > query[ctr]) {
                    hi = mid;
                }
                
                else {
                    lo = mid + 1;
                }
            }
            
            printf("%li\n", lo - 1);
        }
    }
    
    else {
        printf("Pat is the Best Tunnel Master!");
    }
    
    return 0;
}
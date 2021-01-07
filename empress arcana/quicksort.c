#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main () {
    unsigned long long int lo, hi, mid;
    int numSeconds;
    
    scanf("%d", &numSeconds);
    
//    printf("%lf", log2(1e7) / 10);
    
    lo = 0;
    hi = 2 * 1e15;
    
    while (lo < hi) {
        mid = lo + (hi - lo) / 2;
        
        if (mid * log2(mid) / 1e8 > numSeconds) {
            hi = mid;
        }
        
        else {
            lo = mid + 1;
        }
    }
    
    printf("%llu", lo - 1);
     
    return 0;
}
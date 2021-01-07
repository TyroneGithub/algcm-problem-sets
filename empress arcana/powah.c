#include <stdio.h>

long int raiseBase (long int base, long int exponent) {
    long int halfExp, palpatinePower, mod = 1e7;
    
    if (exponent == 0) {
        return 1;
    }
    
    else {
        halfExp = exponent / 2;
        palpatinePower = raiseBase(base, halfExp);
        palpatinePower = palpatinePower * palpatinePower % mod;
        
        if (exponent % 2 == 1) {
            palpatinePower *= base;
            palpatinePower %= mod;
        }
        
        return palpatinePower;
    }
}

int main() {
    long int energy, power;
    
    scanf("%li %li", &energy, &power);
    
    printf("%li", raiseBase(energy, power));
    
    return 0;
}
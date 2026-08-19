#include <stdio.h>


int main() {
/* 
 * Count or sum sequence of digits
 * */

    int x;
    scanf("%d", &x);
    
    // Count
    int n = 0;
    while (x) {
        n += 1;
        x /= 10;
    }

    printf("%d", n);

    /* // Sum
     * int s = 0;
     * while (x) {
     *      int digit = x % 10;
     *
     *      s += digit;
     *      x /= 10;
     * }
     * */

    return 0;
}

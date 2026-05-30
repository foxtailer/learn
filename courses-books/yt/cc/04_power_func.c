#include <stdio.h>


int power(int x, int n) { /* raise x to n-th power; n > 0*/
    int i, p;
    p = 1;

    for (i = 1; i <= n; i++)
        p = p * x;
    
    return p;
}
/*
{
    int p;

    for (p = 1; n > 0; --n)
        p = p * x;
    return(p)
}
*/

int main() {
    for (int i = 0; i < 10; i++)
        printf("%d %d %d\n", i, power(2, i), power(-3, i));
}

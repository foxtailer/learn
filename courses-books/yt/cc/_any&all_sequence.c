#include <stdio.h>


int main() {
    int any = 0;
    int all = 1;

    int x;
    scanf("%d", &x);

    while (x) {
        int digit = x % 10;

        any = any || (digit < 5);
        all = all && (digit < 5);
        
        x /= 10;
    }

    printf("Any: %d\n", any); 
    printf("All: %d\n", all); 
}

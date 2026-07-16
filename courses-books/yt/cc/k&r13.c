#include <stdio.h>


// 1.6(1)

int main() {
/* Count digits, white space, and athers */
    int c, i, nwhite, nother;
    int ndigit[10];

    nwhite = nother = 0;

    for (i = 0; i < 10; i++)
        ndigit[i] = 0;

    while ((c = getchar()) != EOF) {  // Ctrl + D
        if (c >=  '0' && c <= '9')  // 0...48...57...255
            // printf("%c", 49)  >> 1
            ++ndigit[c-'0'];  // 49 - 48 = 1
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;
    }

    printf("digits:");

    for (i = 0; i < 10; i++)
        printf("%d: %d\n", i, ndigit[i]);

    printf("\nwhite space = %d, other = %d\n", 
        nwhite, nother);

    return 0;
}


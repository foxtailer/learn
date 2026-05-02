#include <stdio.h>

/*
int main() {
    int c = getchar();
    c++;
    putchar(c);
    putchar('\n');
    return 1;
}
*/

/*
/// ord ///
int main() {
    int c;

    while ((c = getchar()) != EOF) {
        if (c != '\n') {  // Scip \n(10) from terminal buffer
            printf("%i\n", c);
        }
    }
    return 1;
}
*/

/// terminal buffer count ///
/*
int main() {
    long n = 0;
    
    while (getchar() != '\n') {  // for (nc = 0; getchar() != EOF; ++nc)
        n++;                     //      ;  // Empty body 
    }

    putchar(n);
    printf("%d\n", n); 
}
*/

int main() {
    int c;

    while ((c = getchar()) != EOF) {
        putchar(c);
    }
}
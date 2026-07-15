#include <stdio.h>


// 1.5(1)

int main()
/* copy input to output; 1st version */
{
    int c;
    c = getchar();

    while (c != EOF) {
        putchar(c);
        c = getchar();
    }


    // 1.5(2)
    /*
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);
    */
}

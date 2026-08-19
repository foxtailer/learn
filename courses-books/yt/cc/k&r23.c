#include <stdio.h>

/*
         Column: |       |       |       |
         123456781234567812345678123456781
                 9       17      ...
Line: 1  ········one(8)
      2  two·····three(5)
      3  sixteen·seventeen·······eighteen(1)(7)
      4  oneoneontwo(0?)

*/

// Exercise 1.20


#define TABW 8

int main()
/* detab */
{
    int c, pos;

    pos = 0;
    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            pos = 0;
            putchar(c);
        }
        else if (c == '\t') {
            // ns - number of spaces
            for (int ns = TABW - (pos % TABW); ns > 0; --ns) {
                ++p;
                putchar(' ');
            }
        }
        else {
            ++p;
            putchar(c);
        }
    }

    return 0;
}


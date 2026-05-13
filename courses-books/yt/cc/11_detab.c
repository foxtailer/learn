#include <stdio.h>

/*
// Source - https://stackoverflow.com/a/26359600
// Posted by r3mainer
// Retrieved 2026-04-22, License - CC BY-SA 3.0

\tone\ntwo\tthree\nsixteen\tseventeen\teighteen\n


         Column: |       |       |       |
         123456789012345678901234567890123
Line: 1  ········one
      2  two·····three
      3  sixteen·seventeen·······eighteen

*/

// Source - https://stackoverflow.com/a/69503681
// Posted by Lyon Ma
// Retrieved 2026-04-22, License - CC BY-SA 4.0


#define TABW 8

int main()
{
    int c, p;

    p = 0;
    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            p = 0;
            putchar(c);
        }
        else if (c == '\t') {
            for (int ns = TABW - (p % TABW); ns > 0; --ns) {
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

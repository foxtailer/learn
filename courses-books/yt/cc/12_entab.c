#include <stdio.h>
#define TABW 8

int main() {
    int c, pos;
    int nb = 0; // count of consecutive blanks (spaces)
    int nt = 0; // count of tabs we can use

    for (pos = 1; (c = getchar()) != EOF; ++pos) {
        if (c == ' ') {
            if ((pos % TABW) != 0) {
                ++nb; // just a space, wait to see if it reaches a stop
            } else {
                nb = 0; // we hit a tab stop! convert the pending spaces...
                ++nt;   // ...into a tab
            }
        } else {
            // Before printing the non-space char, "flush" our saved tabs/spaces
            for (; nt > 0; --nt)
                putchar('\t');
            if (c == '\t') // if the char itself is a tab, clear pending spaces
                nb = 0;
            else
                for (; nb > 0; --nb)
                    putchar(' ');

            putchar(c);
            
            // Reset position logic
            if (c == '\n')
                pos = 0;
            else if (c == '\t')
                pos = pos + (TABW - (pos - 1) % TABW) - 1;
        }
    }
    return 0;
}
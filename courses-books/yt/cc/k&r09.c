#include <stdio.h>


// Exercise 1.9

int main () {
/* Copy input to output but change sequence 
of blank char to one space */
    int c, bf;

    bf = 0;
    
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (!bf) {
                bf = 1;
                putchar(' ');
            } 
        } else {
            bf = 0;
            putchar(c);
        }
    }

    return 0;
}


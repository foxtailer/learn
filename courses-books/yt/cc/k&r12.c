#include <stdio.h>

#define YES 1
#define NO 0


// Exercise 1.12

int main () {
/* Print each words on new line */
    int c, inword;

    inword = NO;
    
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (inword == YES) {
                putchar('\n');
                inword = NO;
            }
        }
        else {
            inword = YES;
            putchar(c);
        }
    }
}


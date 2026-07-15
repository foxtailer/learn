#include <stdio.h>


// Exercise 1.8

int main () {
/* Count blank characters */
    int c, bc;

    bc = 0;
    
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t')
            ++bc;
    }

    printf("Blank characters: %d\n", bc);
}


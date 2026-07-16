#include <stdio.h>


// Exercise 1.14

int main() {
/*Ghist of encounter letters*/
    int c;
    int nchar[26];

    for (int i = 0; i < 26; ++i)
        nchar[i] = 0;
    
    while ((c = getchar()) != EOF) {
        if (c >= 'a' && c <= 'z') {
            ++nchar[c - 'a'];
        } else if (c >= 'A' && c <= 'Z') {
            ++nchar[c - 'A'];
        }
    }

    // Print the visual histogram
    for (i = 0; i < 26; ++i) {
        if (nchar[i] > 0) {
            printf("%c: ", 'a' + i);
            
            // Print a star for each occurrence
            for (j = 0; j < nchar[i]; ++j) {
                putchar('*');
            }
            putchar('\n');
        }
    }

    return 0;
}


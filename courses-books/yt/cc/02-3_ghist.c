#include <stdio.h>


/*Cound digits, space characters and other characters*/
int main() {
    int c;
    int nchar[26];

    for (int i = 0; i < 26; ++i)
        nchar[i] = 0;

    while ((c = getchar()) != EOF) {
        if (c >= 'a' && c <= 'z')
            ++nchar[c - 'a'];
    }

    for (int i = 0; i < 26; ++i)
        if (nchar[i] > 0)
            printf("%c: %d\n", 'a' + i, nchar[i]);

}


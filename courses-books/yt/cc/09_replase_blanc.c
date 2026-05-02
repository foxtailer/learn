#include <stdio.h>

int main() /* count characters in input */
{
    int wi;  // write index
    char c[1000];
    char chr;
    int fs = 0;  // space flag


    while ((chr = getchar()) != EOF && wi < 999) {
        if (chr == ' ' || chr == '\n' || chr == '\t') {
            if (!fs) { 
                c[wi] = chr;
                fs = 1;
                wi++;
            }
        }
        else {
            c[wi] = chr;
            fs = 0;
            wi++;
        }
    }

    c[wi] = '\0';
    printf("\nOutput: \n");
    printf("%s\n", c);
}
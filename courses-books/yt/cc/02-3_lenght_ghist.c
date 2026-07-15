#include <stdio.h>


/*Print lenght ghist of words from iinput
 one _ for each character*/
int main() {
    int c;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t')
            putchar(' ');
        else
            putchar('*');
    }
}

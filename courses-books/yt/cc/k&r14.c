#include <stdio.h>


// Esercise 1.13

int main() {
/*
 * Print lenght ghist of words from input
 * one _ for each character.
 */
    int c;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t')
            putchar(' ');
        else
            putchar('*');
    }
}


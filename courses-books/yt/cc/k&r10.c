#include <stdio.h>


// Exercise 1.10

int main(void)
/*This makes all tab and backspace characters visible.*/
{
    int c;

    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            putchar('\\');
            putchar('t');
        } else if (c == '\b') {
            putchar('\\');
            putchar('b');
        } else if (c == '\\') {
            putchar('\\');
            putchar('\\');
        } else {
            putchar(c);
        }
    }

    return 0;
}


/*
import sys

for line in sys.stdin:
    for c in line:
        if c == '\t':
            sys.stdout.write('\\t')
        elif c == '\b':
            sys.stdout.write('\\b')
        elif c == '\\':
            sys.stdout.write('\\\\')
        else:
            sys.stdout.write(c)
*/


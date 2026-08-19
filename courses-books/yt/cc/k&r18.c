#include <stdio.h>

#define MAXLINE 1000  /* maximum input line size */


// Exercise 1.16

int get_line(char s[], int lim);
void copy(char to[], char from[]);


main() 
/* find longest line. No limit. */
{
    int len;            /* current line length */
    int max;            /* maximum length seen so far */
    char line[MAXLINE]; /* current input line */
    char save[MAXLINE]; /* longest line, saved */

    max = 0;
    while ((len = get_line(line, MAXLINE)) > 0)
        if (len > max) {
            max = len;
            copy(line, save);
        }
    
    if (max > 0) { /* there was a line */
        printf("\n--- Longest Line Details ---\n");
        printf("Total Length: %d characters\n", max);
        printf("Text (truncated to %d chars): %s\n", MAXLINE, save);
    }
    return 0;
}


/* get_line: read a line, return TRUE total length without limits */
int get_line(char s[], int lim)
{
    int c, i;

    // 1. Read characters up to the buffer limit minus 1 (for '\0')
    for (i = 0; i < lim - 1 &&
            (c = getchar()) != EOF && c != '\n'; ++i) {
        s[i] = c;
    }
    
    // Append newline if we caught it within the buffer limit
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0'; // Always safely terminate the string

    // 2. UNLIMITED MECHANISM: If we hit the limit but NOT the end 
    // of line, continue reading and counting characters without 
    // saving them.
    if (c != '\n' && c != EOF) {
        while ((c = getchar()) != EOF && c != '\n') {
            ++i; // Keep tracking the total count
        }
        if (c == '\n') {
            ++i;
        }
    }

    return i; /* Returns the absolute total length */
}


* copy: copy 'from' into 'to'; assume 'to' is big enough */
void copy(char to[], char from[])
{
    int i;
    i = 0;
    while ((to[i] = from[i]) != '\0') {
        ++i;
    }
}


#include <stdio.h>

#define MAXLINE 1000  /* maximum input line size */


// Exercise 1.17

int get_line(char s[], int lim)
/* Print lines longer than 80 char */
{
    int c, i;

    for (i=0; i<lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return(i);
}


int main() 
/* find longest line. No limit. */
{
    int len;            /* current line length */
    char line[MAXLINE]; /* current input line */

    while ((len = get_line(line, MAXLINE)) > 0)
        if (len > 80) {
            printf("%s", line);
        }
    
    return 0;
}


#include <stdio.h>


// Exercise 1.19

int MAXLINE = 100;


void reverse_str(char string[]) {
    int head = 0;
    int tail = 0;
    
    // Finde len of the string.
    while (string[tail] != '\0') 
        tail++;

    // Last char is '\0' so we need index -1.
    tail--;

    while (tail > head) {
        char tmp = string[tail];
        string[tail] = string[head];
        string[head] = tmp;

        head++; tail--;
    }
}


int get_line(s, lim) /* get line into s, return length */
char s[];
int lim;
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
/* Reverse line */
{
    char line[MAXLINE]; /* current input line */
    int len;

    while ((len = get_line(line, MAXLINE)) > 0) {
        reverse_str(line);
        printf("%s\n", line);
    }
}


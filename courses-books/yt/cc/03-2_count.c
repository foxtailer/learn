#include <stdio.h>

#define YES 1
#define NO 0


int main () {
    int c, nc, nw, nl, inword;

    inword = NO;
    nc = nw = nl = 0;
    
    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\n' || c == '\t')
            inword = NO;
        else if (inword == NO) {
            inword = YES;
            ++nw;
        }
    }

    printf("Chr: %d, Word: %d, Line: %d\n", nc, nw, nl);
}

#include <stdio.h>
#include <ctype.h>


void to_lower(str)
char str[]; 
{   
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
}


int main() { /* convert uppercase to lowercase */
    char str[] = "HELLO WORLD!";
    to_lower(str);
    printf("%s", str);
}
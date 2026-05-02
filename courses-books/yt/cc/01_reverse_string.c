#include <stdio.h>


void reverse_strint(char string[]) {
    int head = 0;
    int tail = 0;

    while (string[tail] != '\0') tail++;
    tail--;

    while (tail > head) {
        char tmp = string[tail];
        string[tail] = string[head];
        string[head] = tmp;

        head++; tail--;
    }
}

int main() {
    char string1[] = "hello";
    char string2[] = "helo";
    char string3[] = "";
    reverse_strint(string1);
    reverse_strint(string2);
    reverse_strint(string3);
    printf("%s\n", string1);
    printf("%s\n", string2);
    printf("%s\n", string3);
}

#include <stdio.h>

void number_factors(int x) {
    int devisor = 2;

    while (x != 1) {
        while (x % devisor == 0) {
            printf("%d ", devisor);
            x /= devisor;
        }
        ++devisor;
    }
}

int main() {
    int x;
    scanf("%d", &x);
    number_factors(x);

    return 0;
}

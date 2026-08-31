#include <stdio.h>


# define SIZE 1000


int input_array(int A[], int max_size) {
    int top = 0;

    while (1) {
        int x;
        scanf("%d", &x);

        if (x == 0  || top == max_size) break;
        A[top] = x;
        ++top;
    }

    return top;
}


void print_array(int A[], int N) {
    for (int i = 0; i < N; ++i)
        printf("%d ", A[i]);
    printf("\n");
}


void insert_sort(int A[], int N) {
    for (int i = 1; i < N; ++i) {
        int k = i;

        while (k > 0 && A[k-1] > A[k]) {
            int tmp = A[k-1];
            A[k-1] = A[k];
            A[k] = tmp;
            k--;
        }
    }
}


int main() {
    printf("Enter numbers.");

    int A[SIZE];
    int N;

    N = input_array(A, SIZE);
    insert_sort(A, N);
    print_array(A, N);

    return 0;
}


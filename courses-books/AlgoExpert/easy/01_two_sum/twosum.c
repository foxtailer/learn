#include <stdio.h>
#include <stdlib.h>

void print_result(int *result) {
    if (result == NULL) {
        printf("False\n");
    } else {
        printf("[%d, %d]\n", result[0], result[1]);
        free(result);
    }
}

/* ---------------- O(n) version using hash table ---------------- */

#define TABLE_SIZE 1000

typedef struct Node {
    int key;
    struct Node* next;
} Node;

Node* table[TABLE_SIZE];

int hash(int key) {
    if (key < 0) key = -key;
    return key % TABLE_SIZE;
}

void insert(int key) {
    int index = hash(key);

    Node* new_node = malloc(sizeof(Node));
    new_node->key = key;
    new_node->next = table[index];

    table[index] = new_node;
}

int exists(int key) {
    int index = hash(key);

    Node* current = table[index];

    while (current != NULL) {
        if (current->key == key) {
            return 1;
        }
        current = current->next;
    }

    return 0;
}

int* two_sum(int array[], int length, int target) {

    for (int i = 0; i < TABLE_SIZE; i++) {
        table[i] = NULL;
    }

    for (int i = 0; i < length; i++) {

        int number = array[i];
        int gift = target - number;

        if (exists(gift)) {
            int *result = malloc(2 * sizeof(int));
            result[0] = gift;
            result[1] = number;
            return result;
        }

        insert(number);
    }

    return NULL;
}

/* ---------------- O(n log n) version ---------------- */

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

void quicksort(int arr[], int left, int right) {

    int i = left;
    int j = right;
    int pivot = arr[(left + right) / 2];

    while (i <= j) {

        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;

        if (i <= j) {
            swap(&arr[i], &arr[j]);
            i++;
            j--;
        }
    }

    if (left < j) quicksort(arr, left, j);
    if (i < right) quicksort(arr, i, right);
}

int* two_sum2(int array[], int length, int target) {

    quicksort(array, 0, length - 1);

    int L = 0;
    int R = length - 1;

    while (L < R) {

        int current_sum = array[L] + array[R];

        if (current_sum < target)
            L++;
        else if (current_sum > target)
            R--;
        else {
            int *result = malloc(2 * sizeof(int));
            result[0] = array[L];
            result[1] = array[R];
            return result;
        }
    }

    return NULL;
}

/* ---------------- O(n²) brute force ---------------- */

int* two_sum3(int array[], int length, int target) {

    for (int i = 0; i < length; i++) {

        for (int j = i + 1; j < length; j++) {

            if (array[i] + array[j] == target) {

                int *result = malloc(2 * sizeof(int));
                result[0] = array[i];
                result[1] = array[j];
                return result;
            }
        }
    }

    return NULL;
}

/* ---------------- practice from memory ---------------- */

int* two_sum4(int array[], int length, int target) {

    return NULL;
}

int main() {

    int arr[] = {1,6,2,5,8,-3};
    int length = sizeof(arr) / sizeof(arr[0]);

    print_result(two_sum(arr, length, 10));
    print_result(two_sum2(arr, length, 10));
    print_result(two_sum3(arr, length, 10));
    print_result(two_sum4(arr, length, 10));

    return 0;
}

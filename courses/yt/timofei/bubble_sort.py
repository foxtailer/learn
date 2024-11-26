def bubble_sort(A):
    '''sort list A using selections'''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def buble_sort2(A):
    right_boundery = len(A)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(right_boundery):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                sorted = False
        right_boundery-=1

def test_sort(sort_alg):

    print("Test", sort_alg.__doc__)

    print('test 1')
    A = [2,5,4,3,1,8]
    sort_alg(A)
    print('Ok' if A == sorted(A) else 'Fail')

    print('test 2')
    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    sort_alg(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('test 3')
    A = [2,4,2,4,1,8]
    sort_alg(A)
    print('Ok' if A == sorted(A) else 'Fail')

if __name__ == "__main__":
    test_sort(bubble_sort)
    test_sort(buble_sort2)

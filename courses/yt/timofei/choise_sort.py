def choise_sort(A):
    '''sort list A using choises'''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


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
    test_sort(choise_sort)


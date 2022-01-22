'''
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
'''


### Incomplete solution (50%)

def solution(A, K):
    # write your code in Python 3.6
    fin = []
    if (len(A) == K) or (len(set(A))==1):
        fin = A
    else:
        for i in A:
            if A.index(i) > len(A)-K-1:
                fin.insert(A.index(i)+K-len(A),i)
            elif A.index(i) <= len(A)-K-1:
                fin.insert(A.index(i)+K,i)
    return fin


### Complete solution

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    K = K % len(A)
    return (A[-K:] + A[:-K])

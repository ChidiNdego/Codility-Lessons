"""
Find the smallest positive integer that does not occur in a given sequence.


Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# My original solution below attains 88% - and not 100% (due to time complexity); however, I found a really pretty solution online.

def solution(A):
    # write your code in Python 3.6
    max_n = max(A)
    B = range(1,max_n+2)
    if len(set(B)) == 0:
        return 1
    else:
        return min(set(B) - set(A))


# Pretty solution found online

def solution(A):
    a = set(A)
    count = 1
    while count in a:
        count += 1
    return count
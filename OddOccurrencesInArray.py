'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''


A = [9, 3, 9, 3, 9, 7, 9]

### My solution 100% correct

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    sort_a = sorted(A, reverse=True)
    # print(sort_a)
    j = 0
    while j < len(A):
        if sort_a[j] != sort_a[j+1]:
            return sort_a[j]
        j += 2


### Some other solution online

def solution(A):
    unpaired = set()
    for i in A:
        if i in unpaired:
            unpaired.remove(i)
        else:
            unpaired.add(i)
    # print(unpaired)
    ans = unpaired.pop() if len(unpaired) > 0 else 0
    return ans


### One sleek solution I found online using Bitwise operation
### Link: https://www.geeksforgeeks.org/python-bitwise-operators/?ref=lbp

def solution2(A):
    result = 0
    for number in A:
        result ^= number
    return result


print(solution(A))
print(solution2(A))
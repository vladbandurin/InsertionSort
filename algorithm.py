

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

# a = [2,6,7,5,47,6,1,3]
# print(insertion_sort(a))

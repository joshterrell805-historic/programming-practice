def sort(A, low=0, length=None):
    if length is None:
        length = len(A)

    if length <= 1:
        return

    pivot = low
    pivot_v = A[pivot]
    i = low + 1
    while i < low + length:
        if A[i] < pivot_v:
            A[pivot] = A[i]
            A[i] = A[pivot + 1]
            pivot += 1
        i += 1
    A[pivot] = pivot_v

    sort(A, low, pivot - low)
    sort(A, pivot + 1, low + length - 1 - pivot)

def swap(A, i1, i2):
    temp = A[i2]
    A[i2] = A[i1]
    A[i1] = temp

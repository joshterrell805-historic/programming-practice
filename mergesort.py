def sort(A):
    if len(A) <= 1:
        return

    half = int(len(A) / 2)
    left = A[:half]
    right = A[half:]
    sort(left)
    sort(right)
    merge(A, left, right)

def merge(ret, A, B):
    ret_i = 0
    A_i = 0
    B_i = 0

    while A_i < len(A) and B_i < len(B):
        if A[A_i] <= B[B_i]:
            ret[ret_i] = A[A_i]
            A_i += 1
            ret_i += 1
        else:
            ret[ret_i] = B[B_i]
            B_i += 1
            ret_i += 1
    
    while A_i < len(A):
        ret[ret_i] = A[A_i]
        A_i += 1
        ret_i += 1

    while B_i < len(B):
        ret[ret_i] = B[B_i]
        B_i += 1
        ret_i += 1

def binarySearch(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        elif A[mid] == target:
            return mid
    return -1

if __name__ == "__main__":
    A = [1, 5, 6, 9, 15, 22]
    print("Index of 9: " + str(binarySearch(A, 9)))


def solve(A, B):
        curr = 0
        maxx = 0

        for i in range(B):
            curr += A[i]

        maxx = curr 

        j = len(A)-1 #n-1

        for i in range(B-1, -1, -1):
            curr = curr + A[j] - A[i]
            maxx = max(curr, maxx)

            j -= 1

        return maxx

if __name__ == '__main__':
    arr = [5, -2, 3, 1, 2]
    b = 3
    print(solve(arr, b))


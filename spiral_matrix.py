def spiral_order(matrix):
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = n - 1
    top = 0
    bottom = m - 1

    result = [0] * (m*n)

    index = 0
    direction = 0
    

    while top <= bottom and left <= right:
        print("direction: ", direction)
        if direction == 0:
            for i in range(right+1):
                print("going left to right", matrix[top][i])
                result[index] = matrix[top][i]
                index += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom+1):
                print("going top to bottom", matrix[i][right])
                result[index] = matrix[i][right]
                index += 1
            right -= 1
        elif direction == 2:
            tempRight = right
            for i in range(left, right+1):
                print("going right to left", left, right)
                result[index] = matrix[bottom][right-i]
                index += 1
            bottom -= 1
        else:
            print(bottom)
            for i in range(top, bottom):
                tmp = 0
                print("going bottom to top", matrix[bottom-tmp][left])
                result[index] = matrix[bottom-tmp][left]
                tmp += 1
                index += 1
            left += 1
        direction = (direction + 1) % 4
    return result

if __name__=="__main__":
    matrix = [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7],
    ]

    sp = spiral_order(matrix)
    print(sp)


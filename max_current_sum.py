"""Maximum Sum Contiguous Subarray"""
def max_current_sum(nums):
    currentSum = 0
    maxSum = -99999

    for i in range(len(nums)):
        currentSum += nums[i]
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0

    return maxSum

if __name__=="__main__":
    A = [-1, -2, 1, 2, 3, -5, 4, 5]
    result = max_current_sum(A)
    print(result)
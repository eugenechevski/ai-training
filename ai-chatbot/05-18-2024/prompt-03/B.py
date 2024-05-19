def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Create an array to store the lengths of the longest increasing subsequences
    # ending at each position
    dp = [1] * n
    
    # Iterate over the array
    for i in range(1, n):
        # For each element, compare it with all previous elements
        for j in range(i):
            # If the current element is greater than the previous element, update the length
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)
def longest_increasing_subsequence(sequence):
    if not sequence:
        return 0

    dp = [1] * len(sequence)

    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
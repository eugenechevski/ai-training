def expand_around_center(left, right, text):
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return text[left+1: right]


def longest_palindrome(s):
    if len(s) < 2:
        return s

    result = ""
    for i in range(len(s)):
        temp_1 = expand_around_center(i, i, s)
        temp_2 = expand_around_center(i, i+1, s)
        result = max(result, temp_1, temp_2, key=len)

    return result


# Test cases
print(longest_palindrome("babad"))  # Output will be "bab"
print(longest_palindrome("cbbd"))  # Output will be "bb"
print(longest_palindrome('racecar'))  # Output will be 'racecar'.
print(longest_palindrome('noon'))     # Output will be 'noon'.
print(longest_palindrome('abba'))     # Output will be 'abba'.

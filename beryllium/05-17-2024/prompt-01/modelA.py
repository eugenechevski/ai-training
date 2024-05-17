def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]

    best_so_far = ""
    for center in range(len(s)):   # Note the change here
        palindrome_from_center_1 = expand_around_center(center, center)
        palindrome_from_center_2 = expand_around_center(center, center+1)
        longer_palindrome = max(palindrome_from_center_1,
                                palindrome_from_center_2, key=len)
        best_so_far = max(best_so_far, longer_palindrome, key=len)

    return best_so_far

print(longest_palindrome("babad")) # "bab"
print(longest_palindrome("cbbd")) # "bb"
print(longest_palindrome("a"))   # "a" 
print(longest_palindrome("racecar")) #"racecar"
print(longest_palindrome("annana")) #"annana"
print(longest_palindrome("abcda")) # "cdc"

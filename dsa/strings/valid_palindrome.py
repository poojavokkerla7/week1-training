def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # skip non-alphanumeric characters
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            # compare characters
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

    return True


# test cases (this makes it execute)
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False

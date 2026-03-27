class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at opposite ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            if not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            elif not s[right].isalnum():
                right -= 1
            # Compare lowercase versions of characters
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                
        return True

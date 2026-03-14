class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False
        
        s = str(x)
        return s == s[::-1]
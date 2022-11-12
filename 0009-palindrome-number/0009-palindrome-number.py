class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_number = 0
        num = x
        while num > 0:
            remainder = num % 10
            reversed_number = reversed_number * 10 + remainder
            num = num //10
            
        if reversed_number == x:
            return True
        return False
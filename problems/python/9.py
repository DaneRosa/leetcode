'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.


The function first checks if the integer is negative. 
Since negative integers cannot be palindromes, 
the function immediately returns False if x is negative.


If x is not negative, the function initializes two variables: res and n. 
The variable res is initialized to 0, while n is initialized to the value of x.


The function then enters a while loop that continues until n becomes 0. 
In each iteration of the loop, the function takes the last digit of n using the modulo
operator and adds it to res multiplied by 10 
(which shifts the digits of res one position to the left). 
The function then divides n by 10 using the floor division operator to remove the last digit.


After the loop ends, 
the function checks if res is equal to x. 
If res is equal to x, then x is a palindrome and the function returns True. 
Otherwise, x is not a palindrome and the function returns False.




'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if x is palindrome
        if x < 0:  # Negative integers cannot be palindromes
            return False
        res, n = 0, x
        while n:
            res = res*10 + n%10
            n //= 10
        return res == x
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution(object):
    def isPalindromeMarwan(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        list_x = [int(z) for z in str(x)]
        
        if len(list_x) == 1:
            return True
        
        print(list_x)
        print(list(reversed(list_x)))
        return list(reversed(list_x)) == list_x
        
    # Python 3   
    def isPalindrome(self, x):
        if x < 0:
            return False
    
        x_str1 = str(x)
        
        x_str2 = ''.join(reversed(x_str1))
        
        if x_str1 == x_str2:
            return True
        
        return False
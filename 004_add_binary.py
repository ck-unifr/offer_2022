# https://leetcode-cn.com/problems/JFETK5/

# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.
 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        if len_a > len_b:
            b = '0'*(len_a - len_b) + b
        else:
            a = '0'*(len_b - len_a) + a
        stack_a, stack_b = list(a), list(b)
        carry = 0
        cur_sum = 0
        output = ''
        while stack_a and stack_b:
            cur_sum = carry + int(stack_a.pop()) + int(stack_b.pop())
            if cur_sum >= 2:
                cur_sum = cur_sum % 2
                carry = 1
            else:
                carry = 0
            output = str(cur_sum) + output
        if carry == 1:
            output = '1' + output
        return output
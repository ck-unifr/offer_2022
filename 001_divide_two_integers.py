# https://leetcode-cn.com/problems/xoh6Oh/

# 剑指 Offer II 001. 整数除法

# 给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

#  

# 注意：

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231−1]。本题中，如果除法结果溢出，则返回 231 − 1
#  

# 示例 1：

# 输入：a = 15, b = 2
# 输出：7
# 解释：15/2 = truncate(7.5) = 7
# 示例 2：

# 输入：a = 7, b = -3
# 输出：-2
# 解释：7/-3 = truncate(-2.33333..) = -2
# 示例 3：

# 输入：a = 0, b = 1
# 输出：0
# 示例 4：

# 输入：a = 1, b = 1
# 输出：1
#  

# 提示:

# -231 <= a, b <= 231 - 1
# b != 0
#  

# 注意：本题与主站 29 题相同：https://leetcode-cn.com/problems/divide-two-integers/

# 29. Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

#  

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#  

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0


def divide(self, dividend: int, divisor: int) -> int:
	is_negative = (dividend < 0) != (divisor < 0)
	divisor, dividend = abs(divisor), abs(dividend)

	quotient = 0
	the_sum = divisor

	while the_sum <= dividend:
		current_quotient = 1
		while (the_sum + the_sum) <= dividend:
			the_sum += the_sum
			current_quotient += current_quotient
		dividend -= the_sum
		the_sum = divisor
		quotient += current_quotient

	return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))





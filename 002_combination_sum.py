# https://leetcode-cn.com/problems/Ygoe9J/

# 剑指 Offer II 081. 允许重复选择元素的组合

# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

#  

# 示例 1：

# 输入: candidates = [2,3,6,7], target = 7
# 输出: [[7],[2,2,3]]
# 示例 2：

# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：

# 输入: candidates = [2], target = 1
# 输出: []
# 示例 4：

# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 示例 5：

# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
#  

# 提示：

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500
#  

# 注意：本题与主站 39 题相同： https://leetcode-cn.com/problems/combination-sum/



# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#  

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
#  

# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

# https://leetcode.com/problems/combination-sum/


from typing import List 

class Solution:
	def combination(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates.sort()
		res = []
		self.dfs(candidates, [], res, target)
		return res

	def dfs(self, candidates: List[int], comb: List[int], res: List[List[int]], target: int):
		if sum(comb) == target:
			res.append(comb)
			return
		for i in range(len(candidates)):
			if comb and sum(comb) + candidates[i] > target:
				return
			self.dfs(candidates[i:], comb + [candidates[i]], res, target)
		return 


if __name__ =='__main__':
	solution = Solution()
	res = solution.combination([2,3,6,7], 7)
	print(res)









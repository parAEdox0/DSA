"""
1. Two Sum
Solved
Easy
Topics: Arrays, Hash Table
Companies: Many
Hint: Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Example:
Input: nums = [1, 2, 3], target = 4
Output: [0, 2] (because nums[0] + nums[2] = 1 + 3 = 4)

Approaches:
1. Brute Force:
   - Use nested loops to check every pair of numbers in the array.
   - Time Complexity: O(n²) - checking all pairs.
   - Space Complexity: O(1) - only storing the result.
   - Pros: Simple to understand and implement.
   - Cons: Inefficient for large arrays.

2. Hash Map (Optimized):
   - Use a hash map to store numbers and their indices in one pass.
   - For each number, check if its complement (target - num) exists in the hash map.
   - Time Complexity: O(n) - single pass through the array.
   - Space Complexity: O(n) - storing up to n elements in the hash map.
   - Pros: Much faster than brute force.
   - Cons: Uses extra space.
"""

class Solution:
    # Method 1: Brute Force Approach
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        """
        Brute force solution using nested loops to find two numbers that sum to target.
        Returns the indices of the two numbers in a list.
        """
        for i in range(len(nums) - 1):  # Outer loop for first number
            for j in range(i + 1, len(nums)):  # Inner loop for second number, ensuring i != j
                if nums[i] + nums[j] == target:  # Check if pair sums to target
                    return [i, j]  # Return indices immediately when found
        return []  # Fallback (though problem guarantees a solution)

    # Method 2: Hash Map Approach
    def twoSumHashMap(self, nums: list[int], target: int) -> list[int]:
        """
        Optimized solution using a hash map to store numbers and their indices.
        Returns the indices of the two numbers in a list.
        """
        hash_map = {}  # Initialize empty hash map (key: number, value: index)
        for i in range(len(nums)):  # Single pass through the array
            complement = target - nums[i]  # Calculate the complement needed
            if complement in hash_map:  # Check if complement exists in hash map
                return [hash_map[complement], i]  # Return complement's index and current index
            hash_map[nums[i]] = i  # Store current number and its index
        return []  # Fallback (though problem guarantees a solution)


solution = Solution()
    
# Test case
nums = [1, 2, 3]
target = 4
    
# Test brute force method
result_brute = solution.twoSumBruteForce(nums, target)
print(f"Brute Force Result: {result_brute}")  
    
# Test hash map method
result_hash = solution.twoSumHashMap(nums, target)
print(f"Hash Map Result: {result_hash}")  
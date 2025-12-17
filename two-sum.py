from typing import List  # This makes the code look standard and professional

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers in nums such that they add up to target.
        
        Method: Hash Map (Dictionary)

        Args:
            nums (List[int]): A list of integers.
            target (int): The specific value we want to reach.

        Returns:
            List[int]: A list containing the indices of the two numbers.
        """
        
        # Make a dictionary to store numbers we observe and not fit in the eq (num : index)
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
        
            if complement in seen:

                return [seen[complement], i]
            

            seen[num] = i
            
        return [] # Return empty list if no solution is found


if __name__ == "__main__":

    solver = Solution()
    
    # Test Case 1
    test_nums = [2, 7, 11, 15]
    test_target = 9
    result = solver.twoSum(test_nums, test_target)
    
    print(f"Input: {test_nums}, Target: {test_target}")
    print(f"Output Indices: {result}") 
    
    # Test Case 2
    test_nums_2 = [3, 2, 4]
    test_target_2 = 6
    result_2 = solver.twoSum(test_nums_2, test_target_2)
    
    print(f"\nInput: {test_nums_2}, Target: {test_target_2}")
    print(f"Output Indices: {result_2}") 
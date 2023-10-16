
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements we have seen so far.
        num_indices = {}
        
        # Iterate through the array.
        for i, num in enumerate(nums):
            # Calculate the complement (the number we need to reach the target).
            complement = target - num
            
            # Check if the complement exists in our dictionary.
            if complement in num_indices:
                # If it does, return the indices of the two numbers.
                return [num_indices[complement], i]
            
            # If the complement doesn't exist in the dictionary, store the current number's index.
            num_indices[num] = i
        
        # If no solution is found, return an empty list or handle it as needed.
        return []
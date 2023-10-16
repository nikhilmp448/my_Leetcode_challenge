class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # Create a dictionary to store the last seen index of each character.
        char_index = {}
        max_length = 0
        start = 0  # Start of the current substring
        
        for end, char in enumerate(s):
            # If the character is already in the dictionary and its last seen index is after 'start',
            # update 'start' to the index after the last occurrence of the character.
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the last seen index of the character.
            char_index[char] = end
            
            # Calculate the current substring length.
            current_length = end - start + 1
            
            # Update the maximum length if needed.
            max_length = max(max_length, current_length)
        
        return max_length
        
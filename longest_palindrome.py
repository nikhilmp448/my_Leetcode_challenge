class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Preprocess the string to handle even-length palindromes.
        processed_str = '#'.join('^{}$'.format(s))
        n = len(processed_str)
        P = [0] * n  # Initialize an array to store the palindrome lengths.
        
        C, R = 0, 0  # Center and right boundary of the current palindrome.
        max_len, max_center = 0, 0
        
        for i in range(1, n - 1):
            if i < R:
                mirror_i = 2 * C - i  # Find the mirror of the current index.
                P[i] = min(R - i, P[mirror_i])  # Calculate initial palindrome length.
            
            # Attempt to expand palindrome centered at i.
            while processed_str[i + P[i] + 1] == processed_str[i - P[i] - 1]:
                P[i] += 1
            
            # If the palindrome at i expands past R, adjust center and R.
            if i + P[i] > R:
                C, R = i, i + P[i]
                
                # Update the longest palindrome found so far.
                if P[i] > max_len:
                    max_len, max_center = P[i], i
        
        # Extract the longest palindrome from the processed string.
        start = (max_center - max_len) // 2
        end = start + max_len
        return s[start:end]

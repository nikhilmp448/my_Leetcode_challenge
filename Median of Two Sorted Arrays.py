class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine the two sorted arrays into one sorted array
        combined = sorted(nums1 + nums2)
        n = len(combined)
        
        # Check if the combined array has an even or odd length
        if n % 2 == 0:
            # If even, return the average of the middle two elements
            middle1 = combined[n // 2]
            middle2 = combined[n // 2 - 1]
            median = (middle1 + middle2) / 2.0
        else:
            # If odd, return the middle element
            median = combined[n // 2]
        
        return median
    

    

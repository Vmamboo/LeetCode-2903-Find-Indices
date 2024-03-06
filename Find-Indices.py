
def findIndices(nums, indexDifference: int, valueDifference: int):
    # Iterate through each index-value pair in the 'nums' list
    for index, value in enumerate(nums):
        # Store the index and value of the current element
        i1 = index
        val1 = value
        # Iterate through each index-value pair again to find a pair that satisfies the conditions
        for index, num in enumerate(nums):
            # Check if the absolute difference in indices and values satisfy the conditions
            if abs(i1 - index) >= indexDifference and abs(val1 - num) >= valueDifference:
                # If conditions are met, return the indices of the pair
                return [i1, index]
    # If no suitable pair is found, return [-1, -1]
    return [-1, -1]

# Example usage:
nums1 = [5, 1, 4, 1]
indexDifference1 = 2
valueDifference1 = 4
print(findIndices(nums1, indexDifference1, valueDifference1))  # Output: [0, 3]

nums2 = [2, 1]
indexDifference2 = 0
valueDifference2 = 0
print(findIndices(nums2, indexDifference2, valueDifference2))  # Output: [0, 0]

nums3 = [1, 2, 3]
indexDifference3 = 2
valueDifference3 = 4
print(findIndices(nums3, indexDifference3, valueDifference3))  # Output: [-1, -1]
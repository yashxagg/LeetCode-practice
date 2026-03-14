class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map will store: {number: index}
        hash_map = {}
        
        for i, num in enumerate(nums):
            # Calculate what we need to reach the target
            complement = target - num
            
            # Check if that number exists in our 'seen' dictionary
            if complement in hash_map:
                # Return the index of the complement and the current index
                return [hash_map[complement], i]
            
            # If not found, record this number and its index
            hash_map[num] = i
            
        return []
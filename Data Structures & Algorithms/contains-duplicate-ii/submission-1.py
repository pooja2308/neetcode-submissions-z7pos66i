class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indice_dict = {}
        for index, num in enumerate(nums):
            if num in indice_dict:
                if index - indice_dict[num] <= k:
                    return True
            indice_dict[num] = index
        return False


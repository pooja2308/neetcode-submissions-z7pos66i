class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n1 in nums1:
            res.append(self.get_next_value(n1, nums2))
        return res


    
    def get_next_value(self, n, nums2):
        index = nums2.index(n)
        for num in nums2[index + 1:]:
            if num > n:
                return num
        return -1

                
        
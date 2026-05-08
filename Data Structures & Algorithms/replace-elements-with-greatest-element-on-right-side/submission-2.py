class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    #     replaced = []
    #     for i in range(len(arr)):
    #         maxx = self.helper(arr[i+1:])
    #         replaced.append(maxx)
    #     return replaced

    # def helper(self, list1):
    #     maxx = -1
    #     for i in range(len(list1)):
    #         if list1[i] > maxx: 
    #             maxx = list1[i]
    #     return maxx
        max_right = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(current, max_right)
        return arr




            
            


        
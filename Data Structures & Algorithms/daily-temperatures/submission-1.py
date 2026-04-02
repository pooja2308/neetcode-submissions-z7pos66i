class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stackk = [] # pair [temp, index]
        result = [0] * len(temperatures) 
        for i, t in enumerate(temperatures):
            while stackk and t > stackk[-1][0]:
                stackkT, stackkInd = stackk.pop()
                result[stackkInd] = (i - stackkInd)
            stackk.append([t, i])  
        return result
             

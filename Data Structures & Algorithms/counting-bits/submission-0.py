class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            result = bin(i).count('1')
            output.append(result)
        return output

        
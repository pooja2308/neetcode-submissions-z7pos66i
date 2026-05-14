class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # shift left so that the last iteration dont add shifted left after adding
            res <<= 1

            # add the rightmost bit of n
            res = res | (n & 1)
            
            # shift the n to right to get the next bit
            n >>= 1
        return res

        

        
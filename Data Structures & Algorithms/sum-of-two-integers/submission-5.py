class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff      # 32 bits of 1s
        max_int = 0x7fffffff   # max positive 32-bit int
        while (b != 0):
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        return a if a < max_int else ~(a ^ mask)
    
        
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stackk = []
        for oper in operations:
            
            if stackk and oper == "+":
                stackk.append(stackk[-2] + stackk[-1])
            elif stackk and oper == "D":
                stackk.append(2 * stackk[-1])
            elif stackk and oper == "C":
                stackk.pop()
            else:
                stackk.append(int(oper))
        return sum(stackk)
        
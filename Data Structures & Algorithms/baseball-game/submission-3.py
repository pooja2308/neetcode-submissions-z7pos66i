class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stackk = []
        for oper in operations:
            if stackk and oper == "+":
                stackk.append(int(stackk[-1]) + int(stackk[-2]))
            elif stackk and oper == "D":
                stackk.append(int(stackk[-1]) * 2)
            elif stackk and oper == "C":
                stackk.pop()
            else:
                stackk.append(int(oper))
        return sum(stackk)
                

            
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stackk = []
        for log in logs:
            if log == "../":
                if stackk:
                    stackk.pop()
            elif log == "./":
                continue
            else:
                stackk.append(log)
            
        return len(stackk)

            

        
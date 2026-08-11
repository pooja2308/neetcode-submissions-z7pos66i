class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # using stack
        # time complexity - O(n)
        # space complexity - O(n)
        # stackk = []
        # for log in logs:
        #     if log == "../":
        #         if stackk:
        #             stackk.pop()
        #     elif log == "./":
        #         continue
        #     else:
        #         stackk.append(log)
            
        # return len(stackk)

        # using counter
        # time complexity - O(n)
        # space complexity - O(1)
        counter = 0
        for log in logs:
            if log == "../":
                if counter:
                    counter -= 1
            elif log == "./":
                    continue
            else:
                counter += 1
        return counter

            

        
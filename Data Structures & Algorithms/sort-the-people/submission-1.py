class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # mapp = dict()
        res = []
        # for i in range(len(names)):
        #     mapp[heights[i]] = names[i]

        # for k, v in sorted(mapp.items(), key=lambda item: item[0], reverse=True):
        #     res.append(v)
        
        # return res
        
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
            




            



        
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_citizen = []
        for detail in details:
            if detail[10] in ('F', 'M', 'O'):
                detail = detail.split(detail[10])
                if int(detail[-1][:2]) > 60:
                    senior_citizen.append(detail[-1][:2])
        return len(senior_citizen)
        
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        x = y = 0
        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            elif move == 'W':
                x -= 1
            
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
        
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [[0,0]]
        point = [0,0]
        for d in path:
            match d:
                case 'N':
                    point[1] += 1
                case 'S':
                    point[1] -= 1
                case 'E':
                    point[0] += 1
                case _:
                    point[0] -= 1
            if point in paths:
                return True
            else:
                paths.append(point[:])
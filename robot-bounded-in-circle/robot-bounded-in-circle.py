class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [0, 1]
        pos = [0, 0]
        for i in instructions:
            if i == 'G':
                pos[0], pos[1] = pos[0] + dir[0], pos[1] + dir[1]
            elif i == 'L':
                dir[0], dir[1] = dir[1], -dir[0]
            else:
                dir[0], dir[1] = -dir[1], dir[0]
        if dir[1] == 1 and pos !=[0, 0]:
            return False
        return True
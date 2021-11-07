class Solution:
    def robotSim(self, commands: List[int], obstacles):
        obstacles = {(i[0], i[1]):None for i in obstacles}
        dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        posx, posy = 0, 0
        ind = 0
        ma = 0
        for i in commands:
            if i == -2:
                ind = (ind+1)%4
            elif i == -1:
                ind = (ind-1)%4
            else:
                for j in range(i):
                    if (posx + dir[ind][0], posy + dir[ind][1]) in obstacles:
                        break
                    else:
                        posx += dir[ind][0]
                        posy += dir[ind][1]
                ma = max(ma, posx**2 + posy**2)
        return ma
            
        
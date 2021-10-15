class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        for i in asteroids:
            if i>0:
                arr.append(i)
            else:
                flag = False
                while arr and arr[-1]>0 and  arr[-1]<=abs(i):
                    if arr.pop() == abs(i):
                        flag = True
                        break
                        
                if ((not arr) or (arr and arr[-1]<0)) and not flag:
                    arr.append(i)
        return arr
            
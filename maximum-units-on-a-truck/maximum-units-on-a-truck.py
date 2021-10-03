class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True,key = lambda x:x[1])
        s = i = 0
        while truckSize>=0 and i<len(boxTypes):
            s+= min(truckSize, boxTypes[i][0]) * boxTypes[i][1]
            truckSize-=min(truckSize, boxTypes[i][0])
            i+=1
        return s
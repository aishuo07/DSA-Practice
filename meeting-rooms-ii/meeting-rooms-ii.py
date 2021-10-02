class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        room = 0
        endi = 0
        for i in start:
            if i<end[endi]:
                room += 1
            else:
                endi+=1
        return room
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in bookings:
            arr[i[0]-1] += i[2]
            arr[i[1]] -= i[2]
        s = 0
        for i in range(n):
            s += arr[i]
            arr[i] = s
        return arr[:-1]
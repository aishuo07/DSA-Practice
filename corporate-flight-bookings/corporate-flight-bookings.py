class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort()
        c = sorted(bookings, key = lambda x:x[1])
        j = 0
        k = 0
        m = len(bookings)
        arr = []
        s = 0
        a= []
        for i in range(1, n+1):
            while k<m and i>=bookings[k][0]:
                s+=bookings[k][2]
                k+=1
            while j<k and i>c[j][1]:
                s-=c[j][2]
                j+=1
            arr.append(s)

        return arr
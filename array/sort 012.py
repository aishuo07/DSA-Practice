
def sort012(arr,n):
    arr.sort()

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

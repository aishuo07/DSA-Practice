class Solution:
    def findKthLargest(self, nums, k):
        arr = []
        def heapify(i):
            l = 2*i+1
            r = 2*i+2
            ind = i
            if l<len(arr) and arr[l]<arr[ind]:
                ind = l
            if r<len(arr) and arr[r]<arr[ind]:
                ind = r
            if ind != i:
                arr[ind], arr[i] = arr[i], arr[ind]
                heapify(ind)
        def heapifyins(i):
            parent = (i-1)//2
            ind = i
            if parent>=0 and arr[parent]>arr[ind]:
                ind = parent
            if ind != i:
                arr[ind], arr[i] = arr[i], arr[ind]
                heapifyins(ind)
        
            
        def insert(element):
            arr.append(element)
            heapifyins(len(arr)-1)

        def delete():
            arr[0], arr[-1] = arr[-1], arr[0]
            arr.pop()
            heapify(0)

        for i in nums:
            insert(i)
            if len(arr)>k:
                delete()
        return min(arr)
            
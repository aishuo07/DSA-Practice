
class Solution:
    def middle(self,A,B,C):
        #code here
        if (A<C and A>B) or (A>C and A<B):
            return A
        if (B<C and B>A) or (B<A and B>C):
            return B
        if (C<A and C>B) or (C>A and C<B):
            return C


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends

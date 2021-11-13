class Solution:
    def maxProfit(self, inventory, orders):
        def calc(n):
            return (n*(n+1))//2
        inventory.sort(reverse = True)
        i = 1
        ans= 0
        while orders>0:
            if i<len(inventory) and orders>(i)*(inventory[i-1]-inventory[i]):
                ans += (i)*(calc(inventory[i-1]) - calc(inventory[i]))
                orders -= (i)*(inventory[i-1] - inventory[i])
            else:
                times = orders//(i)
                orders = orders%i
                ans += i*(calc(inventory[i-1]) - calc(inventory[i-1]-times))
                ans += orders*(inventory[i-1]-times)
                orders = 0
            i+=1
        return ans%1000000007
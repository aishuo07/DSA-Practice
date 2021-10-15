class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [1000,900, 500, 400, 100, 90, 50,40, 10,9, 5, 4, 1]
        symbol = ["M", "CM",  "D", "CD","C","XC", "L", "XL","X","IX", "V","IV", "I"]
        i = 0
        ans = ''
        while num:
            ans += (num//arr[i])*symbol[i]
            num%=arr[i]
            i+=1
        return ans
            
            
                    
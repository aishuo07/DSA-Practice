class Solution:
    def numberToWords(self, num: int) -> str:
        arr = [10**9, 10**6, 10**3, 1]
        a = ["Billion", "Million", "Thousand", ""]
        c = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}
        i = 0
        s = ''
        while i<len(arr):
            val = num//arr[i]
            num%=arr[i]
            if val:
                hund = val//100
                if hund:
                    s+=c[hund] + ' ' + "Hundred" + " "
                val -= hund*100
                if val in c:
                    s+=c[val] + ' '
                    val = 0        
                tens = val//10
                if tens:
                    s+=c[tens*10] + ' '
                    val -= tens*10
                if val:
                    s += c[val] + ' '
                s+=a[i] + ' '
            i+=1
        return s.rstrip(' ') or "Zero"
                        
                        
                
                    
                    
                
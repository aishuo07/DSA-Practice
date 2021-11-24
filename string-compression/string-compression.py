class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        while i<len(chars):
            j = i
            while i<len(chars) and chars[j] == chars[i]:
                i+=1
            if i-j == 1:
                chars[k] = chars[j]
                k+=1
            else:
                chars[k] = chars[j]
                k+=1
                for l in str(i-j):
                    chars[k] = l
                    k+=1
        return k
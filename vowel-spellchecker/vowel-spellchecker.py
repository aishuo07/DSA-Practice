class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        dic = {}
        s = set(wordlist)
        cap = {}
        oth = {}
        for i in wordlist:
            if i.lower() not in cap:
                cap[i.lower()] = i
            if ''.join([j if j not in 'aeiou' else '.' for j in i.lower()]) not in oth:
                oth[''.join([j if j not in 'aeiou' else '.' for j in i.lower()])] = i
        arr = []
        for i in queries:
            if i in s:
                arr.append(i)
            elif i.lower() in cap:
                arr.append(cap[i.lower()])
            elif ''.join([j if j not in 'aeiou' else '.' for j in i.lower()]) in oth:
                arr.append(oth[''.join([j if j not in 'aeiou' else '.' for j in i.lower()])])
            else:
                arr.append('')
        return arr
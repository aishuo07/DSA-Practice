class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        d = defaultdict(list)
        for i in sorted(zip(username, timestamp, website), key = lambda x:x[1]):
            d[i[0]].append(i[2])
        c = Counter()
        for i in d:
            c += Counter(set(itertools.combinations(d[i], 3)))
        l = [[-c[i], i] for i in c]
        l.sort()
        return l[0][1]
            
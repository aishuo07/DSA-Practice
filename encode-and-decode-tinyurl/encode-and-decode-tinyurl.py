class Codec:
    def __init__(self):
        self.decod = {}
        self.count = 0
    def encode(self, longUrl: str) -> str:
        self.decod["http://tinyurl.com/" + str(self.count)] = longUrl
        self.count += 1
        return "http://tinyurl.com/" + str(self.count-1)
        

    def decode(self, shortUrl: str) -> str:
        return self.decod[shortUrl]
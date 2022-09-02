# leetcode submit region begin(Prohibit modification and deletion)
class Codec:
    def __init__(self):
        self.id = 0
        self.hashtable = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shorturl = 'http://tinyurl.com/' + str(self.id)
        self.hashtable[shorturl] = longUrl
        self.id += 1
        return shorturl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashtable[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# leetcode submit region end(Prohibit modification and deletion)

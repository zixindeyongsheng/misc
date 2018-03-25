#!/Users/wangjinghui/anaconda3/bin/python3
class palindromic(object):
    class node(object):
        def __init__(self, val, ways = 0):
            self.val = val
            self.jump = [-1, 0]
            self.ways = ways
    
    def trans(self, raw_elem):
        return list(map(lambda x: self.node(x), raw_elem))
    
    def __init__(self, inp = None):
        self.raw = inp
        self.len = len(inp)
        self.paldict = {}
    
    def get_paldict(self):
        self.to_do = [self.node('First')] + self.trans(self.raw)
        self.to_do.append(self.node('Last', 1))
        self.to_do[-2].ways = 1
        i = self.len - 1
        while i > 0:
            for j in self.to_do[i + 1].jump:
                if self.to_do[i].val == self.to_do[i + 2 + j].val:
                    self.to_do[i].jump.append(2 + j)
                    self.paldict[(i - 1, i + 1 + j)] =  self.raw[i - 1: i + 2 + j]
                    print(self.raw[i - 1: i + 2 + j])
                    self.to_do[i].ways += self.to_do[i + 3 + j].ways
            self.paldict[(i-1, i-1)] =  self.raw[i-1: i]
            self.to_do[i].ways += self.to_do[i+1].ways
            i = i -1
        return self.paldict
    
    def get_push_pop_ways(self):
        return self.to_do[1].ways

"""
ID: fuwen.t1
LANG: PYTHON3
TASK: namenum
"""

def int2char(x):
    s = ord('A') + 3 * (x - 2) 
    if x < 7:
        return [chr(s), chr(s+1), chr(s+2)]
    elif x == 7:
        return [chr(s), chr(s+2), chr(s+3)]
    else: 
        return [chr(s+1), chr(s+2), chr(s+3)]


class TrieNode():
    def __init__(self):
        self.children = 26 * [None]
        self.is_leaf = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def char2ind(self, ch):
        return ord(ch) - ord('A')
    
    def insert(self, key):
        n = len(key)
        h = self.root 
        for i in range(n):
            ch = key[i]
            ind = self.char2ind(ch)
            if h.children[ind] is None:
                h.children[ind] = TrieNode()
            h = h.children[ind]
        h.is_leaf = True

    def search(self, node, key, prefix_str):
        if len(key) == 0:
            if node.is_leaf:
                return [prefix_str]
            else:
                return []
        
        x = key[0]
        chrs = int2char(x)
        out = []
        for c in chrs:
            ind = self.char2ind(c)
            if node.children[ind] is None:
                continue
            cands = self.search(node.children[ind], key[1:], prefix_str+c)
            out = out + cands
        return out


fin  = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
fdict = open('dict.txt', 'r')
namedict = fdict.read().rstrip().split()

digits = str(fin.readline().rstrip())
digits = list(map(int, [x for x in digits]))

t = Trie()
for x in namedict:
    t.insert(x)

names = t.search(t.root, digits, '')

if len(names) == 0:
    fout.write('NONE\n')
else:
    for x in names:
        fout.write('%s\n'%x)

fin.close()
fout.close()
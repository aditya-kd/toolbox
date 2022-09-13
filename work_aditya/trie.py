class TrieNode:
    def __init__(self, data):
        self.data = data
        self.child = [None]*26
        self.word_end=0

class Trie:
    def __init__(self):
        self.trie_root= TrieNode('*')

    def insert(self, word):

        curr = self.trie_root
        for i in range(len(word)):
            idx = ord(word[i])- ord('a')
            if curr.child[idx] == None:
                curr.child[idx] = TrieNode(word[i])
            curr = curr.child[idx]
        curr.word_end = 1
        print("INSERTED SUCCESSFULLY")
            

    def search(self, word):
        curr = self.trie_root
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            if curr.child[index] == None:
                print("NOT FOUND")
                return False
            curr = curr.child[index]

        if curr.word_end==1:
                print("Found")
                return True
        print("NOT FOUND")
        return False


    def delete(self, word):
        curr = self.trie_root
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            if curr.child[index] is not None:
                curr = curr.child[index]
            else:
                print("Not able to delete")
                return
        curr.word_end= 0
        print("Word deleted")


trie = Trie()
trie.insert('hello')
trie.insert('bell')
trie.insert('hey')
trie.insert("hell")
trie.search("hello")
trie.delete("hello")
trie.search("hello")

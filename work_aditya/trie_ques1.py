class TrieNode:
    def __init__(self, data):
        self.data = data
        self.count_prefix = 0
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
            curr.count_prefix += 1

        curr.word_end = 1
        print("INSERTED SUCCESSFULLY")

    def delete(self, word):
        if (self.search(word)):
            curr = self.trie_root
            for i in range(len(word)):
                char = word[i]
                index = ord(char) - ord('a')
                curr = curr.child[index]
                if curr.child[index]
                else:
                    print("Not able to delete")
                    return
            if curr.word_end == 1:
                curr.word_end=0
                return "Deleted"
            print("Word deleted")
            return "word not found"


    def countwordswithGivenPrefix(self,prefix):
        curr = self.trie_root

        for i in range(len(prefix)):
            char = prefix[i]
            index = ord(char)-ord('a')
            if curr.child[index] is None:
                return 0

            curr = curr.child[index]

        return curr.count_prefix


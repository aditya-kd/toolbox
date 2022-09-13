def findSuggeest(self, curr, prefix, result):
    if curr.word_end:
        result.append(prefix)
        for i in range(26):
            if curr.child[i] is not None:
                self.findSuggest(curr.child[i], prefix.curr.child[i])
def getAutoSuggestion(self, prefix):
    curr = self.trie_root
    result = []
    for i in range(len(prefix)):
        char = prefix[i]
        index = ord(char) - ord('a')

        if curr.child[index] is not None:
            curr = curr.child[index]

        else:
            return list()

    self.findSuggest(curr, prefix, result)
    return result

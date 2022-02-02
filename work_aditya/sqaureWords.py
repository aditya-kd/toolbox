class Solution:
    def wordSquares(self, words):

        def backtrack(row_no, temp_list,n):

            if len(temp_list)== n:
                x = temp_list[:]
                result.append(x)
                return
            
            prefix = ""
            for word in temp_list:
                prefix+= word[row_no]
            
            prefix_list=[]
          
            if prefix in hash_map:
                prefix_list = hash_map[prefix]

            for word in prefix_list:
                temp_list.append(word)
                backtrack(row_no+1, temp_list, n)
                temp_list.pop()

        result=[]
        hash_map=dict()
        for word in words:
            for i in range(len(word)):
                hash_map[word[0: i+1]]= []
        print(hash_map)
        for word in words:
            for i in range(len(word)):
                hash_map[word[0: i+1]].append(word)
                # hash_map[word[0:i+1]]=hash_map.get(word[0:i+1], list()).append(word)
        print(hash_map)

        for i in range(len(words)):
            temp_list=[]
            temp_list.append(words[i])
            backtrack(1, temp_list, len(words[i]))

        return result
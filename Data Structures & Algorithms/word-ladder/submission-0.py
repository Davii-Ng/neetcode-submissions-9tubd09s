class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS solution 

        Turn the list of words into a graph (adj list)
        If diff(word1, word2) == 1: connect
        BFS over the graph
        if word == end return 
        """
        wordList.append(beginWord) 
        n = len(wordList)
        adj = defaultdict(list)
        
        if endWord not in wordList:
            return 0

        
        
        def checkDiffWord(word1, word2):
            if len(word1) != len(word2):
                return 

            m = len(word1)
            diff = 0
            for i in range(m):
                if word1[i] != word2[i]:
                    diff += 1

            return diff

        for i in range(n):
            for j in range(i+1, n):
                if checkDiffWord(wordList[i], wordList[j]) == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])


        q = deque([beginWord])
        visited = set([beginWord])
        dist = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return dist

                for neighbor in adj[word]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            dist += 1

        return 0
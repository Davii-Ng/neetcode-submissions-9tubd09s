class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        #Construct adj list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] += 1

        
        q =  deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        res = []

        while q:
            node = q.popleft()

            res.append(node)

            for neighbor in graph[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
                    

        return res if len(res) == numCourses else []
            
        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] += 1

        q = deque() 

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        course = 0
        while q:
            course += 1
            
            node = q.popleft()

            for neighbor in graph[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)


        return course == numCourses
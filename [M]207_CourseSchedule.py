class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a course map
        # Go through course map and keep track of tracking, if course already existed in tracking, return false
        tracking = set()
        courseMap = collections.defaultdict(list)
        for prereq in prerequisites:
            courseMap[prereq[0]].append(prereq[1])
        for course in range(numCourses):
            if not self.dfs(course, courseMap, tracking):
                return False
        return True

    def dfs(self, course, courseMap, tracking):
        if course in tracking:
            return False
        tracking.add(course)
        for prereq in courseMap[course]:
            if not self.dfs(prereq, courseMap, tracking):
                return False
        tracking.remove(course)
        courseMap[course] = []
        return True


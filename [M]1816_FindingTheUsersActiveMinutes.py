class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Create a hashmap to keeptrack of user: {user: time}
        # Calculate the UAM based on the created hashmap, using its values
        hashMap = collections.defaultdict(set)
        for log in logs:
            hashMap[log[0]].add(log[1])
        UAMList = [0] * k
        for user in hashMap:
            UAMList[len(hashMap[user])-1] += 1
        return UAMList
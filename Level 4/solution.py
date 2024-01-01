class Graph:
    def _init_(self, banana_list):
        # Initialize the Graph object with a list of trainers and create an adjacency matrix
        self.num_trainers = len(banana_list)
        self.graph = [[0] * self.num_trainers for _ in range(self.num_trainers)]

        # Populate the adjacency matrix based on the dead_lock function
        for i in range(self.num_trainers):
            for j in range(self.num_trainers):
                if i < j:
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]

    def gcd(self, x, y):
        # Helper function to calculate the Greatest Common Divisor (GCD)
        while y:
            x, y = y, x % y
        return x

    def dead_lock(self, x, y):
        # Determine if a deadlock exists between two trainers based on their banana values
        if x == y:
            return 0

        l = self.gcd(x, y)
        if (x + y) % 2 == 1:
            return 1

        x, y = x // l, y // l
        x, y = max(x, y), min(x, y)
        return self.dead_lock(x - y, 2 * y)

    def bpm(self, u, matchR, seen):
        # Helper function to find the maximum number of guard pairs using Bipartite Matching
        for v in range(self.num_trainers):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True

                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def max_guard_pair(self):
        # Find the maximum number of guard pairs using Bipartite Matching
        matchR = [-1] * self.num_trainers
        result = 0
        for i in range(self.num_trainers):
            seen = [False] * self.num_trainers
            if self.bpm(i, matchR, seen):
                result += 1
        return self.num_trainers - 2 * (result // 2)


def solution(banana_list):
    # Create an instance of the Graph class
    graph_instance = Graph(banana_list)
    # Calculate and return the maximum guard pair value
    max_guard_pair = graph_instance.max_guard_pair()

    # Print only the Maximum Guard Pair value

    return max_guard_pair


# # Test cases
# print(solution([1, 7, 3, 21, 13, 19]))
# print(solution([1, 1]))

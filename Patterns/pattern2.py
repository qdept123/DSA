class solution:
    def pattern2(self, N):
        for i in range(1, N+1):
            for j in range(i):
                print("*", end= " ")
            print()
sol = solution()
N = 5
sol.pattern2(N)    
    
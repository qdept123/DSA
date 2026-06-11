class solution:
    def pattern(self, N):
        for i in range(N):
            for j in range(i):
                print("*", end= "")
            print()
    def pattern2(self,N):
        for i in range(N):
            for j in range(N-i-1):
                print("*", end= "")
            print()
sol= solution()
N = 5
sol.pattern(N)
sol.pattern2(N)

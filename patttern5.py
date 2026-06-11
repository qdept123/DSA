class solution:
    def pattern5(self, N):
        for i in range(1, N):
            for j in range(1, N-i+1):
                print("*", end = " ")
            print()
sol = solution()
N= 6
sol.pattern5(N)
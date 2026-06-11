class solution:
    def pattern(self, N):
        for i in range(N):
            #space
            for j in range(N-i-1):
                print(" ", end= "")
            for j in range(2*i+1):
                print("*", end= "")
            for j in range(N-i-1):
                print(" ", end= "")
            print()

sol = solution()
N = 5
sol.pattern(N)


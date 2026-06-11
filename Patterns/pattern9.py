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
    def pattern2(self,N):
        for i in range(N):
            #space
            for j in range(i):
                print(" ", end= "")
            for j in range(2*N-(2*i+1)):
                print("*", end= "")
            for j in range(i):
                print(" ", end= "")
            print()

sol= solution()
N = 5
sol.pattern(N)
sol.pattern2(N)

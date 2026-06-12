class solution:
    def patttern6(self, N):
        for i in range(N):
            for j in range(N,i,-1):
                print(N-j+1, end= " ")
            print()
sol= solution()
N= 5
sol.patttern6(N)
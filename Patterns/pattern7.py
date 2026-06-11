class solution:
    def patttern6(self, N):
        for i in range(1, N):
            for j in range(N-i+1):
                print(j, end= " ")
            print()
sol= solution()
N= 5
sol.patttern6(N)
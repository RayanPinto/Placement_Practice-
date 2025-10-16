def n_queens(n):
    board=["."*n for _ in range(n)]
    print(board)
    drag1=set()
    drag2=set()
    cols=set()
    solutions=[]
    def place(row):
        if row==n:
            solutions.append(board.copy())
            return 
        for col in range(n):
            if col in cols or (row-col) in drag1 or (row+col) in drag2:
                continue
            cols.add(col);drag1.add(row-col);drag2.add(row+col);
            board[row]=board[row][:col]+"Q"+board[row][col+1:]
            place(row+1)
            cols.remove(col);drag1.remove(row-col);drag2.remove(row+col);
            board[row]=board[row][:col]+"."+board[row][col+1:]
    place(0)
    return solutions
sols=n_queens(4)
print(sols)
for i,j in enumerate(sols,1):
    print(f"Number of solution is {i}")
    print("\n".join(j))
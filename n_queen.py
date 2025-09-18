def n_queens(n):
    solutions=[]
    cols=set()
    drag1=set()
    drag2=set()
    board=['.'*n for _ in range(n)]
    print(board)
    def place_queen(row):
        if row==n:
            solutions.append(board.copy())
            print(solutions)
            return 
        for col in range(n):
            if col in cols or (row-col) in drag1 or (row+col) in drag2:
                continue
            cols.add(col);drag1.add(row-col);drag2.add(row+col)
            board[row]=board[row][:col]+'Q'+board[row][col+1:]
            place_queen(row+1)
            cols.remove(col);drag1.remove(row-col);drag2.remove(row+col)
            board[row]=board[row][:col]+'.'+board[row][col+1:]
    place_queen(0)
    return solutions
    
n=4
sols=n_queens(n)
print(sols)
for i,sol in enumerate(sols,1):
    print(f"number of solutions :{len(sols)}")
    print("\n".join(sol))
    print()
    
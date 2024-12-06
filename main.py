import board, pygame, solver

sudoku = board.Board()
sudoku_copy = sudoku.copy_board()
solved_sudoku = solver.Solver(sudoku_copy)
solved_sudoku.solve()
print("sudoku", sudoku.board)
print("solved sudoku", solved_sudoku.board)


running = True
while running:
    sudoku.screen.fill((80, 150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    sudoku.draw_grid()
    
    for row in range(9):
      for col in range(9):
        if sudoku.board[row][col] == 0:
           continue
        else: 
          sudoku.draw_number(row, col, sudoku.board[row][col])

    # update screen
    pygame.display.flip()

pygame.quit()
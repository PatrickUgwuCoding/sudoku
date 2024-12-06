import board, pygame, solver

sudoku = board.Board()
# solved_sudoku = sudoku.copy()
# solved_sudoku = solver.Solver(solved_sudoku)
# solved_sudoku.solve()
# print(solved_sudoku.board)


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
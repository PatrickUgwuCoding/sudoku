import board, pygame, random, solver

# random board
#puzzle = [[random.randint(1,9) for _ in range(9)] for _ in range(9)]
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]


sudoku = board.Board(puzzle)
solved_sudoku = solver.Solver(sudoku)
solved_sudoku.solve()
print(solved_sudoku.board)


running = True
while running:
    sudoku.screen.fill((80, 150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    sudoku.draw_grid()
    
  
    for row in range(9):
      for col in range(9):
        sudoku.draw_number(row, col, solved_sudoku.board[row][col])

    # update screen
    pygame.display.flip()

pygame.quit()
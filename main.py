import board, pygame

sudoku = board.Board()

x, y, mistakes = 0, 0, 0
running = True
while running:
    
    sudoku.screen.fill((80, 150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.dict["pos"]
        elif event.type == pygame.KEYDOWN: # key pressed
            if pygame.K_1 <= event.dict["key"] <= pygame.K_9: # key is valid
              num = int(event.dict["unicode"])
              row = y // (sudoku.SCREEN_WIDTH // 9)
              col = x // (sudoku.SCREEN_HEIGHT // 9)

              # check if number is correct
              if num == sudoku.solver.board[row][col]:
                sudoku.board[row][col] = num
              else:
                 mistakes += 1
                 print(mistakes)
            
    if x + y != 0:
      sudoku.draw_input_square(x, y)    
      
    sudoku.draw_grid()
    
    
    # draw sudoku board
    for row in range(9):
      for col in range(9):
        if sudoku.board[row][col] == 0:
           continue
        else: 
          sudoku.draw_number(row, col, sudoku.board[row][col])
          

    # update screen
    pygame.display.flip()

pygame.quit()
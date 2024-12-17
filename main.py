import board, pygame, dbConnection, time

database = dbConnection.MongoDB()

# user authentication
username = input("\nEnter your name: ")
password = input("Enter your password: ")

if not database.find_user(username, password):
  database.add_user(username, password)
  print("\nNew user created")

print(f"\nHello {username}")



sudoku = board.Board()

x, y, mistakes = 0, 0, 0
running = True
won = False
starting_time = time.time()
while running:
    
  sudoku.screen.fill((80, 150, 100))

  # event manager
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

  
  # draw input square after first click        
  if x + y != 0:
    sudoku.draw_input_square(x, y)    
  
  # draw grid
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

  # check if game is won
  if sudoku.board == sudoku.solver.board:
    running = False
    won = True
    ending_time = time.time()

    # calculate time
    score = ending_time - starting_time + 60 * mistakes
    print(score)
    
    # adding new highscores
    if len(highscores:=database.get_highscores()) < 20:
      database.add_highscore(username, score)
    else:
      for top_score in highscores:
        if score > top_score["score"]:
          database.add_highscore(username, score)



while won:
  pygame.draw.rect(sudoku.screen, "black", pygame.Rect(100, 100, 400, 400))
  
  # event manager
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          won = False

  # update screen
  pygame.display.flip()

database.close()
pygame.quit()
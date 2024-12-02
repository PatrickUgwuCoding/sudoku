import board, pygame, random

# random board
puzzle = [[random.randint(1,9) for _ in range(9)] for _ in range(9)]

sudoku = board.Board(puzzle)
print(puzzle)

running = True
while running:
    sudoku.screen.fill((80, 150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sudoku.draw_grid()
    
    # fill in example numbers
    sudoku.draw_number(3,1,1)
    sudoku.draw_number(1,3,5)

    # update screen
    pygame.display.flip()

pygame.quit()
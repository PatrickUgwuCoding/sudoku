import pygame as p
import random as rand
import solver as s

p.init()
p.display.set_caption("Sudoku")


class Board:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.screen = p.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.solver = s.Solver()
        self.solver.solve()
        self.board = self.copy_board()
        self.generate_board()
        

    def draw_grid(self):
        # divide board into 9 cells
        outer_cell_line_width = 10
        for i in range(1,3):
            p.draw.rect(self.screen, "black", p.Rect(0, (i*self.SCREEN_HEIGHT/3) - (outer_cell_line_width), self.SCREEN_WIDTH, outer_cell_line_width))
            p.draw.rect(self.screen, "black", p.Rect((i*self.SCREEN_WIDTH/3) - (outer_cell_line_width / 2), 0, outer_cell_line_width, self.SCREEN_HEIGHT))
        
        # divide each cell into 9 squares
        inner_cell_line_width = 5
        for i in range(1,9):
            p.draw.rect(self.screen, "black", p.Rect(0, (i*self.SCREEN_HEIGHT/9) - (inner_cell_line_width), self.SCREEN_WIDTH, inner_cell_line_width))
            p.draw.rect(self.screen, "black", p.Rect((i*self.SCREEN_WIDTH/9) - (inner_cell_line_width / 2), 0, inner_cell_line_width, self.SCREEN_HEIGHT))

    def draw_number(self, row, col, num):
        # setup number
        number_size = round(self.SCREEN_HEIGHT/9)
        font = p.font.Font(None, number_size)
        number = font.render(str(num), True, (0, 0, 0)) 
        
        # center number into correct square
        width = (col + 1) * self.SCREEN_WIDTH/9 - self.SCREEN_WIDTH/18 - number.get_size()[0]/2
        height = (row + 1) * self.SCREEN_HEIGHT/9 - self.SCREEN_HEIGHT/18 - number.get_size()[1]/2
        self.screen.blit(number, (width, height))

    def draw_input_square(self, x, y):
        inner_cell_line_width = 5
        new_x = (x // (self.SCREEN_WIDTH / 9))
        new_y = (y // (self.SCREEN_HEIGHT / 9))
        p.draw.rect(self.screen, "red", p.Rect(new_x*self.SCREEN_WIDTH/9, new_y*self.SCREEN_HEIGHT/9, self.SCREEN_WIDTH/9 + inner_cell_line_width / 2, self.SCREEN_HEIGHT/9))

    def draw_win(self, username, score, highscore=False):
        # Setup text
        text_size = round(self.SCREEN_HEIGHT / 18)
        font = p.font.Font(None, text_size)

        # determine the text lines
        if highscore:
            lines = [f"{username}", "New Highscore:", f"{score:.2f}"]
        else:
            lines = [f"{username}", f"Score:", f"{score:.2f}"]

        # center each line by height
        total_height = len(lines) * text_size  
        start_height = self.SCREEN_HEIGHT / 2 - total_height / 2

        # display each line
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (100, 50, 100))
            width = self.SCREEN_WIDTH / 2 - text_surface.get_size()[0] / 2 # center each line by width
            height = start_height + i * text_size
            self.screen.blit(text_surface, (width, height))

        # display text to start a new game
        restart_text = font.render("(click to restart)", True, (100, 50, 100))
        width = self.SCREEN_WIDTH/2 - restart_text.get_size()[0] / 2
        height =  self.SCREEN_HEIGHT/2 + 4 * text_size
        self.screen.blit(restart_text, (width, height))

    
    def generate_board(self):
        difficulty = 30 # low number == low difficulty

        while difficulty > 0:
            rand_row = rand.randint(0, 8)
            rand_col = rand.randint(0, 8)
            
            self.board[rand_row][rand_col] = 0
                    
            difficulty -= 1
        return self.board
    
    def copy_board(self):
        list = [row[:] for row in self.solver.board ]
        return list

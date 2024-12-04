import pygame as p

p.init()
p.display.set_caption("Sudoku")


class Board:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    def __init__(self,board):
        self.screen = p.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.board = board

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
        # set up number
        number_size = round(self.SCREEN_HEIGHT/9)
        font = p.font.Font(None, number_size)
        number = font.render(str(num), True, (0, 0, 0)) 
        
        # center number into correct square
        width = (col + 1) * self.SCREEN_WIDTH/9 - self.SCREEN_WIDTH/18 - number.get_size()[0]/2
        height = (row + 1) * self.SCREEN_HEIGHT/9 - self.SCREEN_HEIGHT/18 - number.get_size()[1]/2
        self.screen.blit(number, (width, height))



    
    

    

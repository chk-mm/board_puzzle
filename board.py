from turtle import Turtle

FONT = ('verdana', 30, 'normal')
STARTING_X = -120
STARTING_Y = 100
SPACE = 80


class Board():

    def __init__(self, screen):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(STARTING_X, STARTING_Y)
        self.screen = screen
        self.tiles = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [15, 12, 14, None]
        ]
        self.completed_tiles = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]
        self.void_pos = (3, 3)
        self.draw_tiles()

    def draw_tiles(self):
        self.turtle.clear()
        self.turtle.goto(STARTING_X, STARTING_Y)
        for row in self.tiles:
            for col in row:
                self.turtle.write(f'{col}', align='center', font=FONT)
                self.turtle.goto(self.turtle.xcor() + SPACE, self.turtle.ycor())
            self.turtle.goto(STARTING_X, self.turtle.ycor() - SPACE)

    def go_up(self):
        up_to_void_pos = (self.void_pos[0] - 1, self.void_pos[1])
        self.swap_with_void(up_to_void_pos)

    def go_down(self):
        up_to_void_pos = (self.void_pos[0] + 1, self.void_pos[1])
        self.swap_with_void(up_to_void_pos)

    def go_left(self):
        up_to_void_pos = (self.void_pos[0], self.void_pos[1] - 1)
        self.swap_with_void(up_to_void_pos)

    def go_right(self):
        up_to_void_pos = (self.void_pos[0], self.void_pos[1] + 1)
        self.swap_with_void(up_to_void_pos)

    def swap_with_void(self, up_to_void_pos):
        x1, y1 = up_to_void_pos
        x2, y2 = self.void_pos
        self.tiles[x2][y2], self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x2][y2]
        self.draw_tiles()
        self.void_pos = up_to_void_pos
        self.screen.update()
import sys

import pygame as py
import random as rnd

start = True
py.init()
rec_size = 20                                                               # change to change the size of rec & screen
x_lines = 60                                                                # change to change the x size of screen
y_lines = 45                                                                # change to change the y size of screen
screen_size = (rec_size * x_lines, rec_size * y_lines)
dark_grey = (30, 30, 30)
cur_dir = 0
prev_dir = 0
keyup = True
display = py.display.set_mode(screen_size)                                  # we start the pygame screen
game_o = False


# ------------------------------------------------------ snake ------------------------------------------------------- #


def convert_coord(x, y):
    x_max = screen_size[0] / rec_size
    y_max = screen_size[1] / rec_size
    if x > x_max or y > y_max or y < 0 or x < 0:
        print("THESE COORDINATES ARE NOT POSSIBLE")
    else:
        x = x * rec_size
        y = y * rec_size
        return x, y


class Snake:

    def __init__(self):
        self.snek = []
        self.snek_head = ()
        snake = py.image.load('./images/snake_body_img.png')
        self.snek_img = py.transform.scale(snake, (rec_size, rec_size))
        snake = py.image.load('./images/snake_head_img.png')
        self.snek_head_img = py.transform.scale(snake, (rec_size, rec_size))
        snake = py.image.load('./images/food_img.png')
        self.food_img = py.transform.scale(snake, (rec_size, rec_size))
        self.prev_dir = 0
        self.food = self.gen_food()
        half_x = int((screen_size[0] / rec_size) / 2)
        half_y = int((screen_size[1] / rec_size) / 2)
        self.snek_head = (half_x, half_y)
        self.snek.append((half_x, half_y + 1))
        self.snek.append((half_x, half_y + 2))

    def draw(self):
        global display
        display.fill(dark_grey)
        for body in self.snek:
            display.blit(self.snek_img, (convert_coord(body[0], body[1])))
        display.blit(self.snek_head_img, (convert_coord(self.snek_head[0], self.snek_head[1])))
        try:
            display.blit(self.food_img, (convert_coord(self.food[0], self.food[1])))
        except TypeError:
            pass
        return display

    def move(self, direction):
        global keyup, game_o
        boolean = False
        if direction != 4:
            self.prev_dir = direction
            match direction:
                case 0:                                                     # 0 = UP
                    self.snek.insert(0, self.snek_head)
                    self.snek_head = (self.snek_head[0], self.snek_head[1] - 1)
                case 1:                                                     # 1 = LEFT
                    self.snek.insert(0, self.snek_head)
                    self.snek_head = (self.snek_head[0] - 1, self.snek_head[1])
                case 2:                                                     # 2 = RIGHT
                    self.snek.insert(0, self.snek_head)
                    self.snek_head = (self.snek_head[0] + 1, self.snek_head[1])
                case 3:                                                     # 3 = DOWN
                    self.snek.insert(0, self.snek_head)
                    self.snek_head = (self.snek_head[0], self.snek_head[1] + 1)

            boolean = True

        else:
            self.move(self.prev_dir)

        if self.snek_head in self.snek:
            game_o = True
        if self.snek_head[0] < 0 or self.snek_head[0] > x_lines:
            game_o = True
        if self.snek_head[1] < 0 or self.snek_head[1] > y_lines:
            game_o = True

        if self.eat():
            self.food = self.gen_food()
        elif boolean:
            try:
                self.snek.pop()
            except IndexError:
                pass

    def eat(self):
        if self.food == self.snek_head:
            return True
        else:
            return False

    def gen_food(self):
        x = rnd.randint(1, x_lines - 1)
        y = rnd.randint(1, y_lines - 1)
        nf = (x, y)
        if nf not in self.snek:
            print(nf)
            return nf
        else:
            self.gen_food()


def game_over():
    global display
    game_over_img = py.image.load('./images/game_over_img.png')
    game_over_quit_img = py.image.load('./images/game_over_quit_img.png')
    game_over_try_again_img = py.image.load('./images/game_over_try_again_img.png')
    x_h = (screen_size[0] / 2) - 75
    y_h = (screen_size[1] / 2) - 30
    display.blit(game_over_img, (x_h, y_h))
    x_h = (screen_size[0] / 2) - 65
    y_h = (screen_size[1] / 2) + 30
    display.blit(game_over_try_again_img, (x_h, y_h))
    ta = game_over_try_again_img.get_rect()
    ta.topleft = (x_h, y_h)
    x_h = (screen_size[0] / 2) + 15
    y_h = (screen_size[1] / 2) + 30
    display.blit(game_over_quit_img, (x_h, y_h))
    g_quit = game_over_quit_img.get_rect()
    g_quit.topleft = (x_h, y_h)
    return ta, g_quit


def click(rec_one, rec_two, pos):
    rec_one_pressed = False
    rec_two_pressed = False
    if rec_one.collidepoint(pos):
        if py.mouse.get_pressed()[0] == 1:                             # rec_one_pressed if mouse pressed on rec_one
            rec_one_pressed = True                                     # Ture = u clicked it else False
    elif rec_two.collidepoint(pos):
        if py.mouse.get_pressed()[0] == 1:                             # same as for rec_one
            rec_two_pressed = True

    return rec_one_pressed, rec_two_pressed

# ------------------------------------------------------ input ------------------------------------------------------- #


def add_keys(event):                                                    # here we add the keys upon the key being
    global cur_dir, keyup                                    # pressed into the cur_dir list
    match event.key:
        case py.K_w:                                                    # W-Key = UP = 0
            if keyup and cur_dir != 3:
                cur_dir = 0
                keyup = False
        case py.K_a:                                                    # A-Key = LEFT = 1
            if keyup and cur_dir != 2:
                cur_dir = 1
                keyup = False
        case py.K_d:                                                    # D-Key = RIGHT = 2
            if keyup and cur_dir != 1:
                cur_dir = 2
                keyup = False
        case py.K_s:                                                    # S-Key = DOWN = 3
            if keyup and cur_dir != 0:
                cur_dir = 3
            keyup = False


def rm_keys(event):                                                     # here we remove the keys when key is no longer
    global cur_dir, keyup                                               # pressed from the cur_dir list
    match event.key:
        case py.K_w:                                                    # W-Key = UP = 0
            if 0 == cur_dir:
                keyup = True
        case py.K_a:                                                    # A-Key = LEFT = 1
            if 1 == cur_dir:
                keyup = True
        case py.K_d:                                                    # D-Key = RIGHT = 2
            if 2 == cur_dir:
                keyup = True
        case py.K_s:                                                    # S-Key = DOWN = 3
            if 3 == cur_dir:
                keyup = True


# ------------------------------------------------------ main -------------------------------------------------------- #


def main():
    global start, screen_size, cur_dir, keyup, display, game_o
    display.fill(dark_grey)
    running = True
    snake = Snake()
    game_o = False
    cur_dir = 0
    while running:
        pos = py.mouse.get_pos()
        py.display.flip()                                               # we update the screen every time we loop
        snake.move(cur_dir)
        if game_o:
            try_again, game_quit = game_over()
            try_again_c, game_quit_c = click(try_again, game_quit, pos)
            if try_again_c:
                main()
            elif game_quit_c:
                py.time.delay(100)
                sys.exit(0)
        else:
            snake.draw()
        py.time.delay(80)

        for event in py.event.get():                                    # we get the events
            if event.type == py.KEYDOWN:                                # if the event is a key being pressed
                add_keys(event)                                         # we give the event to 'add_keys()' to get which
                pass                                                    # is pressed
            if event.type == py.KEYUP:                                  # we give the event to 'rm_keys()' to remove the
                rm_keys(event)                                          # key from the cur_dir list
            if event.type == py.QUIT:
                running = False
                start = False                                           # we don't call main anymore


while start:
    main()

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------- imports ------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


import random
import pygame as py


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------ global variables -------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


screen_size_full = (900, 900)
screen_size = (int(screen_size_full[0] / 15), int(screen_size_full[1] / 15))
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
r_size = 15


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- par -------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


pass


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- par2 ------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


pass


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- functions ----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


pass


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- main ------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def main():

    py.init()
    display = py.display.set_mode(screen_size_full)
    running = True
    clock = py.time.Clock()
    snake_x = int(screen_size[0]/2) * r_size
    snake_y = int(screen_size[1]/2) * r_size
    snake = [
        [snake_x, snake_y],
        [snake_x, snake_y - 1 * r_size],
        [snake_x, snake_y - 2 * r_size],
    ]

    food = [int(screen_size[0] / 4) * r_size, int(screen_size[1] / 3) * r_size]
    py.draw.rect(display, red, py.Rect(food[0], food[1], r_size, r_size), 0)
    py.display.flip()

    key = py.KEYUP

    while running:
        clock.tick(5)

        # if snake[0][0] in [0, screen_size_full[0]] or snake[0][1] in [0, screen_size_full[1]] or snake[0] in snake[1:]:
        #     quit()

        for o in snake:
            py.draw.rect(display, green, py.Rect(o[0], o[1], r_size, r_size), 0)

        py.display.flip()
        new_head = [snake[0][0], snake[0][1]]
        next_key = -1

        for event in py.event.get():

            if event.type == py.QUIT:
                running = False

            elif event.type == py.KEYDOWN:
                next_key = py.KEYDOWN

            elif event.type == py.KEYUP:
                next_key = py.KEYUP

            elif event.type == py.K_LEFT:
                next_key = py.K_LEFT

            elif event.type == py.K_RIGHT:
                next_key = py.K_RIGHT

            else:
                next_key = -1

        key = key if next_key == -1 else next_key

        if key == py.KEYDOWN:
            new_head[1] += 1 * r_size

        if key == py.KEYUP:
            new_head[1] -= 1 * r_size

        if key == py.K_LEFT:
            new_head[0] -= 1 * r_size

        if key == py.K_RIGHT:
            new_head[0] += 1 * r_size

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, screen_size[0] - 1) * 15,
                    random.randint(1, screen_size[1] - 1) * 15
                ]
                food = nf if nf not in snake else None

            py.draw.rect(display, green, py.Rect(food[0], food[1], r_size, r_size), 0)
            py.display.flip()

        else:
            tail = snake.pop()
            py.draw.rect(display, black, py.Rect(tail[0], tail[1], r_size, r_size))
            py.display.flip()

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------- program start --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


main()


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------- end -------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
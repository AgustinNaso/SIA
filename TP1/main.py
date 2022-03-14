from TP1.algorithms.informed import a_star, local_search
from TP1.algorithms.non_informed import dfs, bfs, iddfs
from TP1.heuristic import misplaced_numbers, manhattan_distance, nilsson_sequence, sequence_sum
from TP1.metrics import Metrics
from board import Board
import random
from node import Node
from state import State
import numpy as np
import pygame


class Rectangle:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


def show_solution(ans_node):
    stack = []
    while ans_node:
        stack.append(ans_node)
        ans_node = ans_node.parent
    while stack:
        stack.pop().print_state()
        print('\n')


def show_steps(solution_node):
    stack = []
    while solution_node.parent:
        stack.append(solution_node)
        solution_node = solution_node.parent
    while stack:
        stack.pop().print_state()
        print('\n')


def shuffle():
    new_table = Board(Board.final_table)
    iterations = random.randint(50, 100)
    for i in range(iterations):
        new_table = random.choice(new_table.next_moves())
    return new_table


# Setup for DFS
board = shuffle()
state = State(board)
node = Node(state, None, 0)
metrics = Metrics("BFS", 0, 0, 0, 0, 0, 0)
non_informed = [dfs, bfs, iddfs]
non_i_names = ['dfs', 'bfs', 'iddfs']
i_names = ['local', 'global', 'a_star']
informed = [local_search, a_star, a_star]
heuristic = None


def f(n):
    return n.depth + heuristic(n)


print('initial state')
node.print_state()

pygame.init()

# Constants

RECT_WIDTH = 150
RECT_HEIGHT = 150
COLOR = (10, 255, 255)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

pygame.display.set_caption("8 Puzzle")
icon = pygame.image.load("puzzle_icon.png")
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('shuffle', True, BLACK_COLOR)
pygame.display.set_icon(icon)
window = (1000, 700)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

number_font = pygame.font.SysFont(None, 64)  # default font, size 16

# Constants

def draw_board():
    for i in range(3):
        for j in range(3):
            if board.table[j][i] != 0:
                pygame.draw.rect(background, COLOR,
                                 (20 + (RECT_WIDTH + 10) * i, 20 + (RECT_HEIGHT + 10) * j, RECT_WIDTH, RECT_HEIGHT))

                # make the number from grid[row][col] into an image
                number_text = str(board.table[j][i])
                number_image = number_font.render(number_text, True, BLACK_COLOR, None)

                # centre the image in the cell by calculating the margin-distance
                margin_x = (RECT_WIDTH - 1 - number_image.get_width()) // 2
                margin_y = (RECT_WIDTH - 1 - number_image.get_height()) // 2

                # Draw the number image
                background.blit(number_image,
                                (20 + (RECT_WIDTH + 10) * i + 2 + margin_x, 20 + (RECT_HEIGHT + 10) * j + 2 + margin_y))
            else:
                pygame.draw.rect(background, BLACK_COLOR,
                                 (20 + (RECT_WIDTH + 10) * i, 20 + (RECT_HEIGHT + 10) * j, RECT_WIDTH, RECT_HEIGHT))

    screen.blit(background, (0, 0))


#### Populate the surface with objects to be displayed ####
#### Blit the surface onto the canvas ####


height = screen.get_height()
width = screen.get_width()
draw_board()
running = True

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                board = shuffle()
                board.print()
        if event.type == pygame.KEYDOWN:
            board = board.swap(2, 1, -1, 0)
            board.print()
            print("\n")

    draw_board()

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, COLOR, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, WHITE_COLOR, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button

    screen.blit(text, (width / 2 + 50, height / 2))
    # updates the frames of the game
    pygame.display.update()

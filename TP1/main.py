import time
from TP1.algorithms.informed import a_star, local_search
from TP1.algorithms.non_informed import dfs, bfs, iddfs
from TP1.heuristic import misplaced_numbers, manhattan_distance, nilsson_sequence, sequence_sum
from TP1.metrics import Metrics
from board import Board
import random
from node import Node
from state import State
from tkinter import *
from tkinter import messagebox
import numpy as np
import pygame


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

pygame.display.set_caption("8 Puzzle")
icon = pygame.image.load("puzzle_icon.png")
pygame.display.set_icon(icon)
window = (1000, 700)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)
height = screen.get_height()
width = screen.get_width()

# Constants
SOLVE_BUTTON_WIDTH = 120
SOLVE_BUTTON_HEIGHT = 50
SOLVE_BUTTON_X = 140
SOLVE_BUTTON_Y = height - 100
SHUFFLE_BUTTON_WIDTH = 120
SHUFFLE_BUTTON_HEIGHT = 50
SHUFFLE_BUTTON_X = SOLVE_BUTTON_X + SOLVE_BUTTON_WIDTH + 20
SHUFFLE_BUTTON_Y = SOLVE_BUTTON_Y
BOARD_MARGIN_TOP = 80
RECT_WIDTH = 150
RECT_HEIGHT = 150
COLOR = (10, 255, 255)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

button_font = pygame.font.Font(None, 35)
shuffle_text = button_font.render('Shuffle', True, BLACK_COLOR)
solve_text = button_font.render('Solve', True, BLACK_COLOR)

title_font = pygame.font.Font(None, 64)
title_text = title_font.render('8 Puzzle', True, COLOR)

dropdown_font = pygame.font.Font(None, 50)
algorithm_dropdown_text = dropdown_font.render('Algorithm: ', True, COLOR)

number_font = pygame.font.SysFont(None, 64)  # default font, size 16


def draw_board():
    for i in range(3):
        for j in range(3):
            if board.table[j][i] != 0:
                pygame.draw.rect(background, COLOR,
                                 (30 + (RECT_WIDTH + 10) * i, BOARD_MARGIN_TOP + (RECT_HEIGHT + 10) * j, RECT_WIDTH,
                                  RECT_HEIGHT))

                # make the number from grid[row][col] into an image
                number_text = str(board.table[j][i])
                number_image = number_font.render(number_text, True, BLACK_COLOR, None)

                # centre the image in the cell by calculating the margin-distance
                margin_x = (RECT_WIDTH - 1 - number_image.get_width()) // 2
                margin_y = (RECT_WIDTH - 1 - number_image.get_height()) // 2

                # Draw the number image
                background.blit(number_image,
                                (30 + (RECT_WIDTH + 10) * i + 2 + margin_x,
                                 BOARD_MARGIN_TOP + (RECT_HEIGHT + 10) * j + 2 + margin_y))
            else:
                pygame.draw.rect(background, BLACK_COLOR,
                                 (30 + (RECT_WIDTH + 10) * i, BOARD_MARGIN_TOP + (RECT_HEIGHT + 10) * j, RECT_WIDTH,
                                  RECT_HEIGHT))

    screen.blit(background, (0, 0))


def detect_square(x, y):
    i = np.ceil((x - 20) / (RECT_WIDTH + 10))
    j = np.ceil((y - 20) / (RECT_WIDTH + 10))
    return {"i": int(i - 1), "j": int(j - 1)}


def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board.table[j][i] == 0:
                return {"i": int(i), "j": int(j)}


def inside_board(i):
    return 2 >= i >= 0


def valid_swap(i, j, m, n):
    if inside_board(i) and inside_board(j) and inside_board(m) and inside_board(n):
        return (np.abs(i - m) + np.abs(j - n)) == 1
    return 0


def solve(board):
    metrics = Metrics('bfs', 0, 0, 0, 0, 0, 0)
    answer = bfs(Node(State(board), None, 0), metrics)
    stack = []
    while answer:
        stack.append(answer)
        answer = answer.parent
    return stack


#### Populate the surface with objects to be displayed ####
#### Blit the surface onto the canvas ####

class OptionBox:

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected=0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center=rect.center))
            outer_rect = (
            self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1


height = screen.get_height()
width = screen.get_width()
algo_dropdown = OptionBox(
    650, 150, 200, 50, (255, 255, 255), COLOR, pygame.font.SysFont(None, 30),
    ["BFS", "DFS", "IDDFS", "LOCAL SEARCH", "GLOBAL SEARCH", "A STAR"])
heuristic_dropdown = OptionBox(
    650, 150 + 150, 200, 50, (255, 255, 255), COLOR, pygame.font.SysFont(None, 30),
    ["MANHATTAN", "MISPLACED", "NILSSON"])
running = True

pygame.display.flip()
stack = []
solved = 0

while running:
    solving = 0
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            index = detect_square(mouse[0], mouse[1])
            zero_index = find_zero(board)
            if valid_swap(index['i'], index['j'], zero_index['i'], zero_index['j']):
                board = board.swap_with_post(index['j'], index['i'], zero_index['j'], zero_index['i'])

            # if the mouse is clicked on the
            # button the game is terminated
            if SHUFFLE_BUTTON_X <= mouse[0] <= SHUFFLE_BUTTON_X + SHUFFLE_BUTTON_WIDTH \
                    and SHUFFLE_BUTTON_Y <= mouse[1] <= SHUFFLE_BUTTON_Y + SHUFFLE_BUTTON_HEIGHT:
                board = shuffle()
            if SOLVE_BUTTON_X <= mouse[0] <= SOLVE_BUTTON_X + SOLVE_BUTTON_WIDTH \
                    and SOLVE_BUTTON_Y <= mouse[1] <= SOLVE_BUTTON_Y + SOLVE_BUTTON_HEIGHT:
                print("Solving")
                solving = 1
        selected_option = algo_dropdown.update(event_list)
        if selected_option >= 0:
            print(selected_option)

    if solving:
        stack = solve(board)
        solved = 1

    if solved:
        board = stack.pop().state.board
        time.sleep(0.3)
        if not stack:
            solved = 0
    draw_board()


    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if SHUFFLE_BUTTON_X <= mouse[0] <= SHUFFLE_BUTTON_X + SHUFFLE_BUTTON_WIDTH \
            and SHUFFLE_BUTTON_Y <= mouse[1] <= SHUFFLE_BUTTON_Y + SHUFFLE_BUTTON_HEIGHT:
        shuffle_button_rect = pygame.draw.rect(screen, COLOR, [SHUFFLE_BUTTON_X, SHUFFLE_BUTTON_Y, SHUFFLE_BUTTON_WIDTH,
                                                               SHUFFLE_BUTTON_HEIGHT])

    else:
        shuffle_button_rect = pygame.draw.rect(screen, WHITE_COLOR,
                                               [SHUFFLE_BUTTON_X, SHUFFLE_BUTTON_Y, SHUFFLE_BUTTON_WIDTH,
                                                SHUFFLE_BUTTON_HEIGHT])

    if SOLVE_BUTTON_X <= mouse[0] <= SOLVE_BUTTON_X + SOLVE_BUTTON_WIDTH \
            and SOLVE_BUTTON_Y <= mouse[1] <= SOLVE_BUTTON_Y + SOLVE_BUTTON_HEIGHT:
        solve_button_rect = pygame.draw.rect(screen, COLOR,
                                             [SOLVE_BUTTON_X, SOLVE_BUTTON_Y, SOLVE_BUTTON_WIDTH, SOLVE_BUTTON_HEIGHT])

    else:
        solve_button_rect = pygame.draw.rect(screen, WHITE_COLOR,
                                             [SOLVE_BUTTON_X, SOLVE_BUTTON_Y, SOLVE_BUTTON_WIDTH, SOLVE_BUTTON_HEIGHT])

    # superimposing the text onto our button
    shuffle_text_rect = shuffle_text.get_rect()
    shuffle_text_rect.center = shuffle_button_rect.center
    solve_text_rect = solve_text.get_rect()
    solve_text_rect.center = solve_button_rect.center
    screen.blit(shuffle_text, shuffle_text_rect)
    screen.blit(solve_text, solve_text_rect)
    screen.blit(title_text, ((width - title_text.get_width()) / 2, 20))
    screen.blit(algorithm_dropdown_text, (width/2 + 160, 90))
    algo_dropdown.draw(screen)
    pygame.display.flip()


    # updates the frames of the game
    pygame.display.update()

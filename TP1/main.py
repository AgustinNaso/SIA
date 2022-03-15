import json
import time
from algorithms.informed import a_star, local_search
from algorithms.non_informed import dfs, bfs, iddfs
from heuristic import get_heuristic
from metrics import Metrics
from GUI.option_box import OptionBox
from board import Board
import random
from node import Node
from state import State
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

def shuffle():
    new_table = Board(Board.final_table)
    iterations = random.randint(50, 100)
    for i in range(iterations):
        new_table = random.choice(new_table.next_moves())
    return new_table


# Setup for game
board = shuffle()
state = State(board)
node = Node(state, None, 0)
#
algorithm_list = [bfs, dfs, iddfs, local_search, a_star, a_star]
algorithm_names_list = ['BFS', 'DFS', 'IDDFS', 'LOCAL', 'GLOBAL', 'A STAR']
heuristic = get_heuristic(0)


# function to be used as in place of heuristic for a_star
def f(n):
    return n.depth + heuristic(n)


print('initial state')
node.print_state()

# game settings
with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

depth = int(jsonObject['max_depth'])
show_steps_log = bool(jsonObject['show_steps'])


# game UI initialization
pygame.init()
pygame.display.set_caption("8 Puzzle")
icon = pygame.image.load("puzzle_icon.png")
pygame.display.set_icon(icon)
window = (1100, 700)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)
height = screen.get_height()
width = screen.get_width()

# Constants
TITLE_Y = 20
DROPDOWN_TITLE_Y = 90
DROPDOWN_TITLE_X = 615
STATS_Y = 250
STATS_X = 600
STATS_Y_SEPARATOR = 30
STATS_GROUP_Y_SEPARATOR = 30
SOLVE_BUTTON_WIDTH = 120
SOLVE_BUTTON_HEIGHT = 50
SOLVE_BUTTON_X = 60
SOLVE_BUTTON_Y = height - 100
SHUFFLE_BUTTON_WIDTH = 120
SHUFFLE_BUTTON_HEIGHT = 50
SHUFFLE_BUTTON_X = SOLVE_BUTTON_X + SOLVE_BUTTON_WIDTH + 20
SHUFFLE_BUTTON_Y = SOLVE_BUTTON_Y
RESET_BUTTON_WIDTH = 120
RESET_BUTTON_HEIGHT = 50
RESET_BUTTON_X = SHUFFLE_BUTTON_X + SHUFFLE_BUTTON_WIDTH + 20
RESET_BUTTON_Y = SOLVE_BUTTON_Y
BOARD_MARGIN_TOP = 80
RECT_WIDTH = 150
RECT_HEIGHT = 150
COLOR = (255, 192, 203)  # (10, 255, 255)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
A_STAR_IDX = 5
IDDFS_IDX = 2
LAST_NON_INFORMED_IDX = 2
BIG_FONT_SIZE = 64
MEDIUM_FONT_SIZE = 50
SMALL_FONT_SIZE = 33

# UI fonts
button_font = pygame.font.Font(None, SMALL_FONT_SIZE)
shuffle_text = button_font.render('Shuffle', True, BLACK_COLOR)
solve_text = button_font.render('Solve', True, BLACK_COLOR)
stop_text = button_font.render('Stop', True, BLACK_COLOR)
reset_text = button_font.render('Reset', True, BLACK_COLOR)

title_font = pygame.font.Font(None, BIG_FONT_SIZE)
title_text = title_font.render('8 Puzzle', True, COLOR, BLACK_COLOR)

dropdown_font = pygame.font.Font(None, MEDIUM_FONT_SIZE)
algorithm_dropdown_text = dropdown_font.render('Algorithm:', True, COLOR, BLACK_COLOR)
heuristic_dropdown_text = dropdown_font.render('Heuristic:', True, COLOR, BLACK_COLOR)

stats_font = pygame.font.Font(None, SMALL_FONT_SIZE)

number_font = pygame.font.SysFont(None, BIG_FONT_SIZE)

# Game state variables
selected_algorithm = 0
selected_heuristic = 0
algorithm_number = 0
heuristic_number = 0
algorithm_name = ''
metrics_str = ''
last_metrics = ''
table_before_solve = Board(Board.final_table)

# Game UI components
algo_dropdown = OptionBox(
    600, 150, 200, 50, (255, 255, 255), COLOR, pygame.font.SysFont(None, 30),
    algorithm_names_list)
heuristic_dropdown = OptionBox(
    600 + 250, 150, 200, 50, (255, 255, 255), COLOR, pygame.font.SysFont(None, 30),
    ["MANHATTAN", "MISPLACED", "NILSSON"])


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


# in: x and y position of the rectangle, its width and height
# out: a rectangle with its background colored with COLOR or WHITE_COLOR whether if its selected or not
def check_button_hover(x, y, button_width, button_height):
    if x <= mouse[0] <= x + button_width \
            and y <= mouse[1] <= y + button_height:
        button_rect = pygame.draw.rect(screen, COLOR, [x, y, button_width,
                                                       button_height])

    else:
        button_rect = pygame.draw.rect(screen, WHITE_COLOR,
                                       [x, y, button_width,
                                        button_height])
    return button_rect


def solve(board):
    global table_before_solve, heuristic, algorithm_name
    table_before_solve = Board(board.table)
    algorithm = algorithm_list[algorithm_number]
    heuristic = get_heuristic(heuristic_number)
    algorithm_name = algorithm_names_list[algorithm_number]
    metrics = Metrics(algorithm_name, 0, 0, 0, 0, 0, 0)
    stack = []
    if algorithm_number <= LAST_NON_INFORMED_IDX:
        if algorithm_number == IDDFS_IDX:
            answer = algorithm(Node(State(board), None, 0), metrics, depth)
        else:
            answer = algorithm(Node(State(board), None, 0), metrics)
    else:
        if algorithm_number == A_STAR_IDX:
            answer = algorithm(Node(State(board), None, 0), metrics, f)
        else:
            answer = algorithm(Node(State(board), None, 0), metrics, heuristic)
    while answer:
        stack.append(answer)
        answer = answer.parent
    global metrics_str
    global last_metrics
    metrics.set_depth(len(stack))

    if len(metrics_str) > 1:
        last_metrics = str(metrics_str)
    metrics_str = metrics.to_string()

    return stack


running = True
solution_stack = []
solved = 0
print_ans = 0
auxLoca = 0

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
            if RESET_BUTTON_X <= mouse[0] <= RESET_BUTTON_X + RESET_BUTTON_WIDTH \
                    and RESET_BUTTON_Y <= mouse[1] <= RESET_BUTTON_Y + RESET_BUTTON_HEIGHT:
                board = table_before_solve

            if SOLVE_BUTTON_X <= mouse[0] <= SOLVE_BUTTON_X + SOLVE_BUTTON_WIDTH \
                    and SOLVE_BUTTON_Y <= mouse[1] <= SOLVE_BUTTON_Y + SOLVE_BUTTON_HEIGHT:
                # to switch between solve and stop button
                if solved == 0:
                    solving = 1
                else:
                    solved = 0
        selected_algorithm = algo_dropdown.update(event_list)
        if selected_algorithm >= 0:
            algorithm_number = selected_algorithm
            algorithm_name = algorithm_names_list[selected_algorithm]
        selected_heuristic = heuristic_dropdown.update(event_list)
        if selected_heuristic >= 0:
            heuristic_number = selected_heuristic

    if solving:
        solution_stack = solve(board)
        if solution_stack:
            solved = 1
            print_ans = 1

    if solved:
        board = solution_stack.pop().state.board
        if show_steps_log:
            print("---")
            board.print()
        time.sleep(0.3)
        if not solution_stack:
            solved = 0
    draw_board()

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    shuffle_button_rect = check_button_hover(SHUFFLE_BUTTON_X, SHUFFLE_BUTTON_Y, SHUFFLE_BUTTON_WIDTH,
                                             SHUFFLE_BUTTON_HEIGHT)
    reset_button_rect = check_button_hover(RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT)
    solve_button_rect = check_button_hover(SOLVE_BUTTON_X, SOLVE_BUTTON_Y, SOLVE_BUTTON_WIDTH, SOLVE_BUTTON_HEIGHT)

    # superimposing the text onto our button
    shuffle_text_rect = shuffle_text.get_rect()
    shuffle_text_rect.center = shuffle_button_rect.center
    solve_text_rect = solve_text.get_rect()
    stop_text_rect = stop_text.get_rect()
    stop_text_rect.center = solve_button_rect.center
    solve_text_rect.center = solve_button_rect.center
    reset_text_rect = reset_text.get_rect()
    reset_text_rect.center = reset_button_rect.center
    screen.blit(shuffle_text, shuffle_text_rect)
    if solved == 1:
        screen.blit(stop_text, solve_text_rect)
    else:
        screen.blit(solve_text, solve_text_rect)
    screen.blit(reset_text, reset_text_rect)
    screen.blit(title_text, ((width - title_text.get_width()) / 2, TITLE_Y))
    screen.blit(algorithm_dropdown_text, (DROPDOWN_TITLE_X, DROPDOWN_TITLE_Y))
    screen.blit(heuristic_dropdown_text, (DROPDOWN_TITLE_X + 255, DROPDOWN_TITLE_Y))

    if print_ans == 1:
        aux = metrics_str.split('\n')
        for i in range(len(aux)):
            stats = stats_font.render(aux[i], True, COLOR, BLACK_COLOR)
            screen.blit(stats, (STATS_X, STATS_Y + i * STATS_Y_SEPARATOR))
        move_y = len(aux) * STATS_Y_SEPARATOR
        aux = last_metrics.split('\n')
        if len(aux) > 1:
            stats = stats_font.render("Previous solve: ", True, WHITE_COLOR, BLACK_COLOR)
            screen.blit(stats, (STATS_X, STATS_Y + move_y))
            for i in range(len(aux)):
                stats = stats_font.render(aux[i], True, COLOR, BLACK_COLOR)
                screen.blit(stats, (STATS_X, STATS_Y + move_y + STATS_GROUP_Y_SEPARATOR + i * STATS_Y_SEPARATOR))

    algo_dropdown.draw(screen)
    heuristic_dropdown.draw(screen)
    pygame.display.flip()

    # updates the frames of the game
    pygame.display.update()

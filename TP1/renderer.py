import arcade
import numpy as np

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Set the background color to white.
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.

color = 1  # 0 britu 1 gasti
table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

if (color == 0):
    background = arcade.color.PINK
    lines_color = arcade.color.WHITE
elif color == 1:
    background = arcade.color.BLUE
    lines_color = arcade.color.YELLOW
else:
    background = arcade.color.BLACK
    lines_color = arcade.color.WHITE

arcade.set_background_color(background)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# board border
x = 75
y = 75
width = 450
arcade.draw_line(x, y, x + width, y, color=lines_color, line_width=10)
arcade.draw_line(x, y, x, y + width, color=lines_color, line_width=10)
arcade.draw_line(x, y + width, x + width, y + width, color=lines_color, line_width=10)
arcade.draw_line(x + width, y, x + width, y + width, color=lines_color, line_width=10)
increment = width / 3
arcade.draw_line(x + increment, y, x + increment, y + width, color=lines_color, line_width=10)
arcade.draw_line(x + increment * 2, y, x + increment * 2, y + width, color=lines_color, line_width=10)
arcade.draw_line(x, y + increment, x + width, y + increment, color=lines_color, line_width=10)
arcade.draw_line(x, y + increment * 2, x + width, y + increment * 2, color=lines_color, line_width=10)

# arcade.draw_text("1", x + increment / 3, y + increment / 3, lines_color, font_size=50)
for i in range(len(table)):
    for j in range(len(table[i])):
        arcade.draw_text(str(table[i][j]), x + increment / 3 + increment * j, y + increment*2 + increment / 3 - increment * i,
                         lines_color, font_size=50)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

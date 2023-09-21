"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Lab_02")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Draw the sun
arcade.draw_circle_filled(720,520,75, arcade.color.YELLOW_ORANGE)

# --- Draw the house ---

# House cement base
arcade.draw_lrtb_rectangle_filled(150, 600, 190, 170, arcade.color.COOL_GREY)

# Main Level
arcade.draw_lrtb_rectangle_filled(150,600,420,190, arcade.color.ALMOND)

# House Door
arcade.draw_lrtb_rectangle_filled(340,400,290,190, arcade.color.ANTI_FLASH_WHITE)
arcade.draw_circle_filled(350,240,5, arcade.color.ANTIQUE_BRONZE)

# Right Window
arcade.draw_lrtb_rectangle_filled(215, 285,320,250, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(215,285,287,282, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(248,253,320,250, arcade.color.WHITE)

# Left Window
arcade.draw_lrtb_rectangle_filled(465,535,320,250, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(465,535,287,282, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(498,503,320,250, arcade.color.WHITE)

# House Roof
arcade.draw_triangle_filled(380,580,630,420,120,420, arcade.color.COOL_BLACK)

# Walkway
arcade.draw_lrtb_rectangle_filled(295,450,169,0, arcade.color.GRAY)

# --- Draw Trees ---

# Right Side Tree
arcade.draw_lrtb_rectangle_filled(675, 695, 320,170, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(685,335,65, arcade.color.DEEP_MOSS_GREEN)

# Left Side Tree
arcade.draw_lrtb_rectangle_filled(60,80,320,170, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(70,335,65, arcade.color.DEEP_MOSS_GREEN)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
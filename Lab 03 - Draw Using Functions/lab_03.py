import arcade


def draw_house():
    """Draw a House"""

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


def draw_grass():
    """Draw Grass"""

    # Draw the grass
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


def draw_sun():
    """Draw the Sun"""

    # Draw the sun
    arcade.draw_circle_filled(720, 520, 75, arcade.color.YELLOW_ORANGE)


def draw_tree():
    """Draw Trees"""

    # Right Side Tree
    arcade.draw_lrtb_rectangle_filled(675, 695, 320, 170, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(685, 335, 65, arcade.color.DEEP_MOSS_GREEN)

    # Left Side Tree
    arcade.draw_lrtb_rectangle_filled(60, 80, 320, 170, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(70, 335, 65, arcade.color.DEEP_MOSS_GREEN)


def draw_road():
    """Draw the Road"""

    # Draw Road
    arcade.draw_lrtb_rectangle_filled(0, 800, 80, 0, arcade.color.GRAY)


def draw_car(x,y):
    """Draw a Car"""


    # Base
    arcade.draw_lrtb_rectangle_filled(x, 170 + x, 90 + y, 50 + y, arcade.color.BLUEBERRY)

    # Roof
    arcade.draw_lrtb_rectangle_filled(x, 190 + x, 125 + y, 90 + y, arcade.color.BLUEBERRY)

    # Lights
    arcade.draw_lrtb_rectangle_filled(x, 170 + x, 75 + y, 55 + y, arcade.color.WHITE)

    # Windows
    arcade.draw_lrtb_rectangle_filled(x - 15, x + 120, 120 + y, 90 + y, arcade.color.DIM_GRAY)
    arcade.draw_lrtb_rectangle_filled(x + 15, x + 160, 120 + y, 90 + y, arcade.color.DIM_GRAY)

    # Wheels
    arcade.draw_circle_filled(x + 15, 50 + y, 18, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 150, 50 + y, 18, arcade.color.BLACK)



def on_draw(delta_time):
    """Draw Everything"""
    arcade.start_render()

    draw_grass()
    draw_sun()
    draw_house()
    draw_tree()
    draw_road()
    draw_road()
    draw_car(on_draw.car1_x, 20)

    # Add one to the x value, making the car move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.car1_x += 3


    # Create a value that our on_draw.car1_x will start at.

    arcade.finish_render()

def main():
    arcade.open_window(800, 600, "Lab_03")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)


    on_draw.car1_x=50

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)

    # Keep the window up until someone closes it.
    arcade.run()

# Call the main function to get the program started
main()
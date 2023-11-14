""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_background():
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.draw_lrtb_rectangle_filled(150, 600, 190, 170, arcade.color.COOL_GREY)
    arcade.draw_lrtb_rectangle_filled(150, 600, 420, 190, arcade.color.ALMOND)
    arcade.draw_lrtb_rectangle_filled(340, 400, 290, 190, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw_circle_filled(350, 240, 5, arcade.color.ANTIQUE_BRONZE)
    arcade.draw_lrtb_rectangle_filled(215, 285, 320, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(215, 285, 287, 282, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(248, 253, 320, 250, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(465, 535, 320, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(465, 535, 287, 282, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(498, 503, 320, 250, arcade.color.WHITE)
    arcade.draw_triangle_filled(380, 580, 630, 420, 120, 420, arcade.color.COOL_BLACK)
    arcade.draw_lrtb_rectangle_filled(295, 450, 169, 0, arcade.color.GRAY)
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)
    arcade.draw_circle_filled(720, 520, 75, arcade.color.YELLOW_ORANGE)
    arcade.draw_lrtb_rectangle_filled(675, 695, 320, 170, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(685, 335, 65, arcade.color.DEEP_MOSS_GREEN)
    arcade.draw_lrtb_rectangle_filled(60, 80, 320, 170, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(70, 335, 65, arcade.color.DEEP_MOSS_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 800, 80, 0, arcade.color.GRAY)



class Car:
    def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def draw(self, x, y):
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


class MyGame(arcade.Window):
    """ Our Custom Window Class"""


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.position_x = x
        self.position_y = y

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.position_x = 0
        self.position_y = 0
        self.car = Car(10, 10, 10)
        self.crash_sound = arcade.load_sound("qubodup-crash.ogg")
        self.crash_player = None

    def on_draw(self):
        arcade.start_render()
        draw_background()
        self.car.draw(self.position_x, self.position_y)
        print(self.crash_player)
        if self.position_x < 10 or self.position_x > 790:
            if not self.crash_player or not self.crash_player.playing:
                self.crash_player = arcade.play_sound(self.crash_sound)


def main():
    window = MyGame()
    arcade.run()


main()

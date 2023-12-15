import arcade
import random

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.4
ZOMBIE_COUNT = 15
COIN_COUNT = 75


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Final Lab - Zombie Survival"

MOVEMENT_SPEED = 3

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.zombie_list = None
        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.zombie_sprite = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           .2)
        self.player_sprite.center_x = 225
        self.player_sprite.center_y = 60
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Create a row of boxes
        for x in range(0, 800, 63):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = -20
            self.wall_list.append(wall)

        for x in range(0, 800, 63):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                     SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 520
            self.wall_list.append(wall)

        for y in range(0, 800, 63):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = -20
            wall.center_y = y
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(0, 800, 63):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 820
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list = [[90, 135],
                           [90, 80],
                           [145, 135],
                           [145, 80]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list1 = [[345, 135],
                            [455, 135],
                            [290, 135],
                            [510, 135],
                            [565, 135],
                            [235, 135],
                            [345, 80],
                            [455, 80],
                            [290, 80],
                            [510, 80],
                            [565, 80],
                            [235, 80]]

        for coordinate in coordinate_list1:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list2 = [[665, 80],
                            [665, 135],
                            [720, 80],
                            [720, 190]]

        for coordinate in coordinate_list2:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for y in range(245, 400, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = 720
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(170, 620, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = x
            wall.center_y = 245
            self.wall_list.append(wall)

        for y in range(245, 400, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = 610
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(245, 400, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = 168
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(170, 620, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = x
            wall.center_y = 354
            self.wall_list.append(wall)

        for x in range(170, 620, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for y in range(245, 420, 55):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .4)
            wall.center_x = 75
            wall.center_y = y
            self.wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                             .2)
        wall.center_x = 720
        wall.center_y = 435
        self.wall_list.append(wall)

        for x in range(170, 660, 25):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 .2)
            wall.center_x = x
            wall.center_y = 435
            self.wall_list.append(wall)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(ZOMBIE_COUNT):
            zombie = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk6.png", .2)

            zombie_placed_successfully = False

            # Keep trying until success
            while not zombie_placed_successfully:
                # Position the coin
                zombie.center_x = random.randrange(SCREEN_WIDTH)
                zombie.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(zombie, self.wall_list)

                # See if the coin is hitting another coin
                zombie_hit_list = arcade.check_for_collision_with_list(zombie, self.zombie_list)

                if len(wall_hit_list) == 0 and len(zombie_hit_list) == 0:
                    # It is!
                    zombie_placed_successfully = True

            # Add the coin to the lists
            self.zombie_list.append(zombie)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.zombie_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.coin_list == 0:
            output = "YOU WIN"
            arcade.draw_text(output, 400, 250, arcade.color.WHITE, 100)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.coin_list.update()
        self.zombie_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 5
            coin_sound = arcade.load_sound("collectcoin-6075.mp3")
            arcade.play_sound(coin_sound)

        zombie_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.zombie_list)

        for zombie in zombie_hit_list:
            self.score -= 5


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

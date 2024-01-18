import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
    def on_draw(self):

        arcade.start_render()

        arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))

        for i in [0, 1, 2, 3]:
            print("i a pour valeur", i)
            cercle_change_x = +3
            cercle_change_y = +3


def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()


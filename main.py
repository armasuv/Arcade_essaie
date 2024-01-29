import arcade,random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

COLORS = [arcade.color.AERO_BLUE, arcade.color.ALABAMA_CRIMSON, arcade.color.ASPARAGUS, arcade.color.BONDI_BLUE]
class Balle:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rayon = random.randint(10,20)
        self.change_y = random.randint(-5,5)
        self.change_x = random.randint(-5,5)
        self.color = random.choice(COLORS)
    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, radius=self.rayon, color=self.color)
    def update(self):
        self.pos_x += self.change_x

        if self.pos_x > SCREEN_WIDTH:
            self.change_x *= -1
        if self.pos_x < 0:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT:
            self.change_y *= -1
        if self.pos_y < 0:
            self.change_y *= -1
class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

        self.la_liste_de_victor = []

    def on_draw(self):
        arcade.start_render()

        for obj in self.la_liste_de_victor:
            obj.draw()
            obj.update()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.la_liste_de_victor.append(Balle(pos_x = x, pos_y = y))

def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()
main()


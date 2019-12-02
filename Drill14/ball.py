import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1800), random.randint(0, 1100), 0

    def set_background(self, bg):
        self.bg = bg
        # self.x = self.bg.w / 2
        # self.y = self.bg.h / 2

    def get_bb(self):
        # self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def get_rec(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10
    def draw(self):
        self.cx, self.cy = self.x - self.bg.window_left, self.y-self.bg.window_bottom
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_rec())

    def update(self):
        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(0, self.y, self.bg.h)


        self.y -= self.fall_speed * game_framework.frame_time


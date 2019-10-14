from pico2d import*
import random

open_canvas(800,600,True)
running = True
frame = 0


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.type = random.randint(0, 1)
        self.small = load_image('ball21x21.png')
        self.big = load_image('ball41x41.png')
        self.speed = random.randint(5, 15)
        self.fall = True
    def update(self):
        if self.type == 0:
            if self.y - 10.5 > 60.5 and self.fall:
                self.y -= self.speed
            else:
                self.y = 69
                self.fall = False
        elif self.type == 1:
            if self.y - 20.5 > 60.5 and self.fall:
                self.y -= self.speed
            else:
                self.y = 79
                self.fall = False
    def draw(self):
        if self.type == 0:
            self.small.draw(self.x, self.y)
            # draw_rectangle(self.x - 10.5, self.y - 10.5, self.x + 10.5, self.y + 10.5)
        elif self.type == 1:
            self.big.draw(self.x, self.y)
            # draw_rectangle(self.x - 20.5, self.y - 20.5, self.x + 20.5, self.y + 20.5)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()

while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)

import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
flicker = 0


def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

    pass


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if flicker % 3 == 0:
        image.clip_draw(200, 200, 500, 500, 400, 300) # 200 ,200 지점에서 500 500 비율로 출력 400,300 위치에 출력
    update_canvas()
    pass







def update():
    global flicker
    flicker += 1
    delay(0.2)
    pass


def pause():
    pass


def resume():
    pass







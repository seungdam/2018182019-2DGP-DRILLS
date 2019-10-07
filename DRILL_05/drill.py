from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global v, u
    global x2,y2
    global move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            v,u = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
                x2, y2 = event.x, KPU_HEIGHT - 1 - event.y
                move = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass






open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('run_animation.png')
character_left =load_image('run_animation_left.png')
arrow = load_image('hand_arrow.png')

running = True

x2, y2 = KPU_WIDTH // 2, KPU_HEIGHT // 2 #mouse 위치
x1, y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2 #현재위치
u,v = 0,0
move = False
frame = 0

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    arrow.draw(v, u)

    if move:
        for i in range(0, 100 + 1, 2):
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            arrow.draw(v, u)

            t = i / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2

            if x2 > x1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
            elif x2 < x1:
                character_left.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
            handle_events()
            if x == x2 and y == y2:
                x1 = x2
                y1 = y2
                i = 0
                move = False
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
    update_canvas()
    handle_events()

close_canvas()





from pico2d import*
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)

background =load_image('KPU_GROUND.png')
character = load_image('run-right.png')
arrow = load_image('arrow.png')

running = True
frame = 0
frame = 1

player_x = 500
player_y = 500

goto_x = 500
goto_y = 500
cnt = 0

is_right = True
is_moving = False


def draw_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    # draw p1-p2
    global player_x, player_y
    global frame
    for i in range(0, 50, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)
        t = i / 100
        player_x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        player_y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)
        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)
    # draw p3-p4
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)

        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)
    # p4 p5
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)

        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)

    # p5 p6
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)

        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)

    # p6 p7
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)

        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)
    # P7 P8
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)
        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)
    # p8 p9
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)
        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)

    # p9 p10
    for i in range(0, 100, 2):
        clear_canvas()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        arrow.draw(p1[0], p1[1], 50, 50)
        arrow.draw(p2[0], p2[1], 50, 50)
        arrow.draw(p3[0], p3[1], 50, 50)
        arrow.draw(p4[0], p4[1], 50, 50)
        arrow.draw(p5[0], p5[1], 50, 50)
        arrow.draw(p6[0], p6[1], 50, 50)
        arrow.draw(p7[0], p7[1], 50, 50)
        arrow.draw(p8[0], p8[1], 50, 50)
        arrow.draw(p9[0], p9[1], 50, 50)
        arrow.draw(p10[0], p10[1], 50, 50)
        t = i / 100
        player_x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        player_y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        character.clip_draw(frame * 100, 0, 100, 100, player_x, player_y)
        frame = (frame + 1) % 8
        pico2d.update_canvas()
        delay(0.05)

    pass

def handle_events():
    global running

    global is_moving
    global cnt

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False
    pass
def moving_character():
    global goto_x, goto_y
    global player_x, player_y
    global is_moving
    global is_right
    global frame
    global cnt

    t = cnt / 100

    for i in range (0,100,2):
        player_x = (1 - t) * player_x + t * goto_x
        player_y = (1 - t) * player_y + t * goto_y
        cnt += 2
        if player_x - goto_x > 0:
            is_right = False
            frame_y = 0
        else:
            is_right = True
            frame_y = 1
    else:
        is_moving = False
        if is_right:
            frame_y = 1
        else:
            frame_y = 0


pico2d.hide_cursor()

points = [(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000)),(random.randint(1,1000),random.randint(1,1000))]
while(running):
    draw_curve_10_points(points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7],points[8], points[9])
    handle_events()



pico2d.close_canvas()

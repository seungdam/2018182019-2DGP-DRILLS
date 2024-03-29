from pico2d import *
from ball import Ball

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, LSHIFT_DOWN, LSHIFT_UP, RSHIFT_DOWN, RSHIFT_UP = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,


    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
            delay(0.02)
        elif event == LEFT_DOWN:
            boy.velocity -= 1
            delay(0.02)
        elif event == RIGHT_UP:
            boy.velocity -= 1
            delay(0.02)
        elif event == LEFT_UP:
            boy.velocity += 1
            delay(0.02)


    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)




class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame +1) % 8

    @staticmethod
    def draw(boy):
        if boy.velocity >= 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class DashState:
    @staticmethod
    def enter(boy, event):
        if event is RIGHT_DOWN:
            boy.velocity += 1
        elif event is LEFT_DOWN:
            boy.velocity -= 1
        elif event is RIGHT_UP:
            boy.velocity -= 1
        elif event is LEFT_UP:
            boy.velocity += 1

        boy.dir = boy.velocity
        boy.timer_dash = 200

    @staticmethod # 대쉬 상태에서 나가야 하기때문에 키를 때면
    def exit(boy, event):
        if event is LSHIFT_UP or RSHIFT_UP:
            boy.timer_dash = 0

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer_dash -= 1
        boy.x += boy.velocity*2
        boy.x = clamp(25, boy.x, 1600 - 25)

        if boy.timer_dash == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.velocity >= 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, LSHIFT_DOWN : IdleState, LSHIFT_UP : IdleState, RSHIFT_DOWN : IdleState, RSHIFT_UP : IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, LSHIFT_DOWN : DashState, LSHIFT_UP : RunState, RSHIFT_DOWN : DashState, RSHIFT_UP : RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LSHIFT_DOWN : IdleState, LSHIFT_UP : IdleState, RSHIFT_DOWN : IdleState, RSHIFT_UP : IdleState},
    DashState : {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SLEEP_TIMER: RunState, LSHIFT_DOWN : DashState, LSHIFT_UP : RunState, RSHIFT_DOWN : DashState, RSHIFT_UP : RunState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


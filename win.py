from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("YOU WIN!", font='big'),
            int(screen.height / 2) - 8),
        Cycle(
            screen,
            FigletText("CONGRATULATIONS!", font='big'),
            int(screen.height / 2) + 3),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

if __name__ == "__main__":
    Screen.wrapper(demo)

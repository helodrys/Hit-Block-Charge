import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


bomb_frames = [
    """
     ___________________    . , ; .
    (___________________|~~~~~X.;' .
                          ' `" ' `
    """,
    """
     ___________________    . , ; .
    (___________________|~~~~X.;' .
                          ' `" ' `
    """,
    """
     ___________________    . , ; .
    (___________________|~~~X.;' .
                          ' `" ' `
    """,
    """
     ___________________    . , ; .
    (___________________|~~X.;' .
                          ' `" ' `
    """,
    """
     ___________________    . , ; .
    (___________________|~X.;' .
                          ' `" ' `
    """,
    """
     ___________________    . , ; .
    (___________________|X.;' .
                          ' `" ' `
    """
]

final_explosion_lines = [
    "     _.-^^---....,,--",
    " _--                  --_     ",
    "<                        >)   ",
    "|                         |   ",
    " \\._                   _./    ",
    "    ```--. . , ; .--'''       ",
    "          | |   |             ",
    "       .-=||  | |=-.          ",
    "       `-=#$%&%$#=-'          ",
    "          | ;  :|             ",
    " _____.,-#%&$@%#&#~,._____"
]


bold = "\033[1m"
blue = "\033[34m"
red = "\033[31m"
reset = "\033[0m"

def bomb_animation():
    for frame in bomb_frames:
        clear_screen()
        sys.stdout.flush()
        print(frame)

    for i in range(3, 0, -1):
        clear_screen()
        print(f"{bold}{blue}Exploding Zip bomb in {i}...{reset}")
        time.sleep(1)

    clear_screen()


    for i in final_explosion_lines:
        print(f"{bold}{blue}{i}{reset}")
        time.sleep(0.3)
    
    print(f"\n> {red}Zip bomb have triggered!!!{reset}")

if __name__ == "__main__":
    bomb_animation()

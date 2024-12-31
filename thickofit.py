import time
import sys

def charging_animation(repeats=2):
    bold = "\033[1m"
    reset = "\033[0m"

    for _ in range(repeats):
        for dots in range(4):
            animation = f"{bold}> Filling electricity bill{reset}{'.' * dots}{' ' * (3 - dots)}"
            sys.stdout.write(f"\r{animation}")
            sys.stdout.flush()
            time.sleep(0.21)
    print()
    for _ in range(repeats):
        for dots_3 in range(4):
            animation_3 = f"{bold}> Connecting to eletricity{reset}{'.' * dots_3}{' ' * (3 - dots_3)}"
            sys.stdout.write(f"\r{animation_3}")
            sys.stdout.flush()
            time.sleep(0.21)
    print()
    for _ in range(repeats):
        for dots_2 in range(4):
            animation_2 = f"{bold}> Charging{reset}{'.' * dots_2}{' ' * (3 - dots_2)}"
            sys.stdout.write(f"\r{animation_2}")
            sys.stdout.flush()
            time.sleep(0.21)
    print()
    sys.stdout.write(f"\r{bold}> Charging success!{reset}\n")
    # sys.stdout.flush()
    
if __name__ == "__main__":
    charging_animation(repeats=2)
import time
import sys

def download_animation(repeats=2):
    bold = "\033[1m" 
    reset = "\033[0m"

    for _ in range(repeats):
        for dots in range(4):
            animation = f"{bold}Executing{reset}{'.' * dots}{' ' * (3 - dots)}"
            sys.stdout.write(f"\r{animation}")
            sys.stdout.flush()
            time.sleep(0.2)


    sys.stdout.write("\rExecution Complete!\n")
    sys.stdout.flush()

if __name__ == "__main__":
    download_animation(repeats=2)
